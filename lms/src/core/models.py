from django.contrib.auth import get_user_model
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from core.managers import CustomerManager


class UserGender(models.Model):
    gender = models.CharField(max_length=20, null=False, default="Unknown")

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"

    def __str__(self):
        return f"{self.gender}"


class UserType(models.Model):
    type = models.CharField(max_length=30, null=False, default="User")

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return f"{self.type}"


class Customer(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), null=True, blank=True)
    phone_number = PhoneNumberField(_("phone number"), blank=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return f"{self.email}"


class ProxyUser(get_user_model()):
    class Meta:
        proxy = True


class UserProfile(models.Model):
    user = models.OneToOneField(to=get_user_model(), related_name="profile", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="static/img/profiles/", default="static/img/avatar.png/")
    city = models.CharField(max_length=255, null=False, default="Kyiv")
    location = PlainLocationField(based_fields=["city"], zoom=7)
    birth_date = models.DateField(null=True)
    user_type = models.ForeignKey(to=UserType, on_delete=models.CASCADE, null=True, related_name="type_of_user")
    gender = models.ForeignKey(to=UserGender, on_delete=models.CASCADE, null=True, related_name="user_gender")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.pk}_{self.user}"
