from django.core.exceptions import ValidationError


def first_name_validator(first_name: str) -> None:
    if "vova" in first_name.lower():
        raise ValidationError("Vova is not correct name, should be Volodymyr!!!")


def grade_validator(grade: int) -> None:
    if grade not in range(1, 12):
        raise ValidationError("Should be in range 1-11")
