from django.core.exceptions import ValidationError


def amount_students_validator(amount_students: int) -> None:
    if amount_students not in range(24, 34):
        raise ValidationError("Should be in range 24 - 33!!!")
