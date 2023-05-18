from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "groups_count", "links_to_groups")
    list_display_links = ("first_name", "last_name", "email", "groups_count", "links_to_groups")
    fieldsets = (
        ("Personal information", {"fields": ("first_name", "last_name", "email")}),
        ("Additional information", {"classes": ("collapse",), "fields": ("birth_date", "group")}),
    )

    def groups_count(self, obj):
        if obj.group:
            return obj.group.count()
        return 0

    def links_to_groups(self, obj):
        if obj.group:
            groups = obj.group.all()
            links = []
            for group in groups:
                links.append(
                    f"<a class='button' href='{reverse('admin:groups_group_change', args=[group.pk])}'"
                    f">{group.group_name}</a>"
                )
            return format_html("<br><br>".join(links))
        return "No groups found"
