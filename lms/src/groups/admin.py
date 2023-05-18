from django.contrib import admin

from groups.forms import GroupAdminForm
from groups.models import Group
from students.models import Students
from teachers.models import Teacher


class StudentAdminInline(admin.TabularInline):
    model = Students
    extra = 0


class TeacherAdminInline(admin.TabularInline):
    model = Teacher.group.through
    extra = 0


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    actions = ("count_to_zero",)
    inlines = (StudentAdminInline, TeacherAdminInline)
    list_display = (
        "group_name",
        "faculty",
        "head_teacher",
    )
    list_display_links = (
        "group_name",
        "faculty",
        "head_teacher",
    )

    @admin.action(description="Set to zero of count of selected groups")
    def count_to_zero(self, request, queryset):
        queryset.update(amount_students=0)
