from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from core.models import UserProfile, UserType, UserGender


class ProfileAdminInline(admin.TabularInline):
    model = UserProfile
    extra = 0


@admin.register(UserType)
class TypeAdmin(admin.ModelAdmin):
    list_filter = ("type",)


@admin.register(UserGender)
class GenderAdmin(admin.ModelAdmin):
    list_filter = ("gender",)


@admin.register(get_user_model())
class CustomerAdmin(UserAdmin):
    inlines = (ProfileAdminInline,)
    date_hierarchy = "date_joined"
    fields = ("first_name", "last_name", "password", "phone_number", "email", "is_staff", "is_active", "date_joined")
    ordering = ("first_name",)
    fieldsets = None
    readonly_fields = ("email", "phone_number")
    list_display = ("first_name", "last_name", "phone_number", "email", "is_staff", "is_active", "date_joined")
    list_display_links = ("first_name", "last_name", "phone_number", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff",)
    search_fields = ("first_name", "phone_number", "email")
