from django.contrib import admin

from students.models import Students


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    date_hierarchy = "birth_date"
    ordering = ("group",)
    list_display = (
        "first_name",
        "last_name",
        "email",
        "group",
    )
    list_display_links = (
        "first_name",
        "last_name",
        "email",
        "group",
    )
    list_filter = ("group__group_name", "email")
    search_fields = ("first_name__istartswith", "email")
