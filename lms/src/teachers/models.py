import random

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from core.utils.teacher_validators import (
    teacher_first_name_validator,
    teacher_last_name_validator,
    teacher_experience_years_validator,
)


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=120, null=True, validators=[MinLengthValidator(2), teacher_first_name_validator]
    )
    last_name = models.CharField(
        max_length=120, null=True, validators=[MinLengthValidator(2), teacher_last_name_validator]
    )
    email = models.EmailField(max_length=120, null=True)
    experience_years = models.PositiveIntegerField(
        default=3, null=True, validators=[teacher_experience_years_validator]
    )
    birth_date = models.DateField(null=True)
    subject = models.CharField(max_length=120, null=True)
    group = models.ManyToManyField(to="groups.Group")
    avatar = models.ImageField(upload_to="static/img/", blank=True, null=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "All teachers"

    def __str__(self):
        return f"{self.pk} {self.first_name}_{self.last_name} ({self.subject})"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        subject = [
            "PE",
            "Math",
            "Chemistry",
            "Art",
            "History",
            "Music",
            "English",
            "Geography",
        ]

        for _ in range(count):
            cls.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                experience_years=random.randint(3, 7),
                birth_date=faker.date_time_between(start_date="-55y", end_date="-30y"),
                subject=random.choice(subject),
            )
