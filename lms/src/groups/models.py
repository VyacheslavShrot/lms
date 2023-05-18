import random

from django.core.validators import MaxLengthValidator

from django.db import models

from faker import Faker

from core.utils.groups_validators import amount_students_validator


class Group(models.Model):
    group_name = models.CharField(max_length=120, null=True, validators=[MaxLengthValidator(2)])
    amount_students = models.PositiveIntegerField(default=30, null=True, validators=[amount_students_validator])
    head_teacher = models.CharField(max_length=120, null=True)
    faculty = models.CharField(max_length=120, null=True)
    head_teacher_email = models.EmailField(max_length=120, null=True)
    head_teacher_phone = models.CharField(max_length=120, null=True)

    class Meta:
        verbose_name = "Groups"
        verbose_name_plural = "All groups"

    def __str__(self):
        return f"{self.pk} {self.group_name}_{self.faculty} ({self.head_teacher})"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        group_name = ["A", "B", "C", "D"]
        faculty = [
            "Dept. of IT",
            "Department of Biology",
            "Dept. of Chemistry",
            "Dept. of Physics",
            "Dept. of PE",
        ]

        for _ in range(count):
            cls.objects.create(
                group_name=random.choice(group_name),
                amount_students=random.randint(24, 33),
                head_teacher=f"{faker.first_name()}_{faker.last_name()}",
                faculty=random.choice(faculty),
                head_teacher_email=faker.email(),
                head_teacher_phone=faker.phone_number(),
            )
