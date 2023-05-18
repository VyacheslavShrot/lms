# Generated by Django 3.2.16 on 2023-01-23 01:12

import django.core.validators
from django.db import migrations, models

import core.utils.teacher_validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "first_name",
                    models.CharField(
                        max_length=120,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            core.utils.teacher_validators.teacher_first_name_validator,
                        ],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=120,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            core.utils.teacher_validators.teacher_last_name_validator,
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=120, null=True)),
                (
                    "experience_years",
                    models.PositiveIntegerField(
                        default=3,
                        null=True,
                        validators=[core.utils.teacher_validators.teacher_experience_years_validator],
                    ),
                ),
                ("birth_date", models.DateField(null=True)),
                ("subject", models.CharField(max_length=120, null=True)),
                ("group", models.ManyToManyField(to="groups.Group")),
            ],
        ),
    ]
