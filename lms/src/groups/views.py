from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from webargs import fields

from webargs.djangoparser import use_kwargs

from groups.forms import GroupForm

from groups.models import Group


class GetGroupView(LoginRequiredMixin, TemplateView):
    template_name = "groups/groups_list.html"
    model = Group

    @use_kwargs(
        {
            "group_name": fields.Str(required=False),
            "faculty": fields.Str(required=False),
            "search_text": fields.Str(required=False),
        },
        location="query",
    )
    def get(self, request, **kwargs):
        groups = Group.objects.all()

        search_fields = ["group_name", "faculty", "head_teacher"]

        for field_name, field_value in kwargs.items():
            if field_name == "search_text":
                or_filter = Q()

                for field in search_fields:
                    or_filter |= Q(**{f"{field}__contains": field_value})

                groups = groups.filter(or_filter)

            else:
                if field_value:
                    groups = groups.filter(**{field_name: field_value})

        return render(request, template_name="groups/groups_list.html", context={"groups": groups})


class CreateGroupView(LoginRequiredMixin, CreateView):
    template_name = "groups/group_create.html"
    form_class = GroupForm
    success_url = reverse_lazy("groups:get_groups")
    queryset = Group.objects.all()


class UpdateGroupView(LoginRequiredMixin, UpdateView):
    template_name = "groups/groups_update.html"
    form_class = GroupForm
    success_url = reverse_lazy("groups:get_groups")
    queryset = Group.objects.all()


class DeleteGroupView(LoginRequiredMixin, UpdateView, DeleteView):
    template_name = "groups/groups_delete.html"
    form_class = GroupForm
    success_url = reverse_lazy("groups:get_groups")
    queryset = Group.objects.all()


class GetGroupsTeachersView(LoginRequiredMixin, TemplateView):
    template_name = "groups/groups_teachers.html"
    model = Group

    def get(self, request, pk):
        group = get_object_or_404(Group.objects.all(), pk=pk)

        return render(request, template_name="groups/groups_teachers.html", context={"group": group})
