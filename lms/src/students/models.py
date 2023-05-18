import datetime

import random

from uuid import uuid4

from django.core.validators import MinLengthValidator

from django.db import models

from faker import Faker

from groups.models import Group

from core.utils.student_validators import first_name_validator, grade_validator


class Students(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True, db_index=True)
    first_name = models.CharField(max_length=120, null=True, validators=[MinLengthValidator(2), first_name_validator])
    last_name = models.CharField(max_length=120, null=True, validators=[MinLengthValidator(2)])
    email = models.EmailField(max_length=120, null=True)
    grade = models.PositiveIntegerField(default=0, null=True, validators=[grade_validator])
    birth_date = models.DateField(null=True)
    department = models.CharField(max_length=300, null=True)
    group = models.ForeignKey(to=Group, related_name="all_students_in_this_group", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="static/img/", blank=True, null=True)
    summary = models.FileField(upload_to="files/", blank=True, max_length=200)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "All students"
        ordering = (
            "-first_name",
            "last_name",
        )

    def age(self):
        return datetime.datetime.now().year - self.birth_date.year

    def __str__(self):
        return f"{self.first_name}_{self.last_name} ({self.grade})"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()

        for _ in range(count):
            cls.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                grade=random.randint(1, 11),
                birth_date=faker.date_time_between(start_date="-30y", end_date="-18y"),
            )
