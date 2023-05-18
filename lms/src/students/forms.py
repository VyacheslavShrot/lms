from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Students


class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ("first_name", "last_name", "email", "grade", "birth_date", "department", "group")

    @staticmethod
    def normalize_text(text: str) -> str:
        return text.strip().capitalize()

    def clean_email(self):
        email = self.cleaned_data["email"]

        if "@yandex" in email:
            raise ValidationError("Yandex domain is forbidden in our country!!!")

        return email

    def clean_last_name(self):
        return self.normalize_text(self.cleaned_data["last_name"])

    def clean_first_name(self):
        return self.normalize_text(self.cleaned_data["first_name"])

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data["first_name"]
        last_name = cleaned_data["last_name"]

        if first_name == last_name:
            raise ValidationError("First name and last name cant be equal")

        return cleaned_data
