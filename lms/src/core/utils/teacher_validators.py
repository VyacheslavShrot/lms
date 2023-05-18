from django.core.exceptions import ValidationError


def teacher_first_name_validator(first_name: str) -> None:
    if "slavik" in first_name.lower():
        raise ValidationError("Slavik is not correct name, should be Vyacheslav!!!")


def teacher_last_name_validator(last_name: str) -> None:
    if len(last_name) > 9:
        raise ValidationError("Too big input last name((")


def teacher_experience_years_validator(experience_years: int) -> None:
    if experience_years not in range(3, 8):
        raise ValidationError("Should be in range 3 - 7!!!")
