import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from students.forms import StudentForm

from students.models import Students

from webargs import fields

from webargs.djangoparser import use_kwargs


class GetStudentsView(LoginRequiredMixin, TemplateView):
    template_name = "students/students_list.html"
    model = Students

    @use_kwargs(
        {
            "first_name": fields.Str(required=False),
            "last_name": fields.Str(required=False),
            "search_text": fields.Str(required=False),
        },
        location="query",
    )
    def get(self, request, **kwargs):
        students = Students.objects.all()

        search_fields = ["first_name", "last_name", "email"]

        for field_name, field_value in kwargs.items():
            if field_name == "search_text":
                request.session[f"search_text_{datetime.datetime.now()}"] = field_value

                or_filter = Q()

                for field in search_fields:
                    # accumulate filter condition
                    or_filter |= Q(**{f"{field}__contains": field_value})

                students = students.filter(or_filter)

            else:
                if field_value:
                    students = students.filter(**{field_name: field_value})

        return render(request, template_name="students/students_list.html", context={"students": students})


def search_history(request):
    log_list = {}
    for key, value in request.session.items():
        if "search_text" in key:
            log_list.update({key: value})

    return render(request, template_name="search_history.html", context={"search_history": log_list})


class CreateStudentView(LoginRequiredMixin, CreateView):
    template_name = "students/students_create.html"
    form_class = StudentForm
    success_url = reverse_lazy("students:get_students")
    initial = {"grade": 1}


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    template_name = "students/students_update.html"
    form_class = StudentForm
    success_url = reverse_lazy("students:get_students")
    pk_url_kwarg = "uuid"
    queryset = Students.objects.all()


class DeleteStudentView(LoginRequiredMixin, UpdateView, DeleteView):
    template_name = "students/students_delete.html"
    form_class = StudentForm
    success_url = reverse_lazy("students:get_students")
    pk_url_kwarg = "uuid"
    queryset = Students.objects.all()
