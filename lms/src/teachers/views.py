from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from webargs import fields

from webargs.djangoparser import use_kwargs

from teachers.forms import TeacherForm

from teachers.models import Teacher


class GetTeacherView(LoginRequiredMixin, TemplateView):
    template_name = "teachers/teachers_list.html"
    model = Teacher

    @use_kwargs(
        {
            "first_name": fields.Str(required=False),
            "last_name": fields.Str(required=False),
            "search_text": fields.Str(required=False),
        },
        location="query",
    )
    def get(self, request, **kwargs):
        teachers = Teacher.objects.all()

        search_fields = ["first_name", "last_name", "subject"]

        for field_name, field_value in kwargs.items():
            if field_name == "search_text":
                or_filter = Q()

                for field in search_fields:
                    or_filter |= Q(**{f"{field}__contains": field_value})

                teachers = teachers.filter(or_filter)

            else:
                if field_value:
                    teachers = teachers.filter(**{field_name: field_value})

        return render(request, template_name="teachers/teachers_list.html", context={"teachers": teachers})


class CreateTeacherView(LoginRequiredMixin, CreateView):
    template_name = "teachers/teachers_create.html"
    form_class = TeacherForm
    success_url = reverse_lazy("teachers:get_teachers")


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    template_name = "teachers/teachers_update.html"
    form_class = TeacherForm
    success_url = reverse_lazy("teachers:get_teachers")
    queryset = Teacher.objects.all()


class DeleteTeacherView(LoginRequiredMixin, UpdateView, DeleteView):
    template_name = "teachers/teachers_delete.html"
    form_class = TeacherForm
    success_url = reverse_lazy("teachers:get_teachers")
    queryset = Teacher.objects.all()
