# Generated by Django 3.2.16 on 2023-02-19 21:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0005_alter_students_group"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="students",
            options={
                "ordering": ("-first_name", "last_name"),
                "verbose_name": "Student",
                "verbose_name_plural": "All students",
            },
        ),
    ]