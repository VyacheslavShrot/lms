from django.urls import path

from students.views import (
    CreateStudentView,
    UpdateStudentView,
    DeleteStudentView,
    GetStudentsView,
)

app_name = "students"

urlpatterns = [
    path("", GetStudentsView.as_view(), name="get_students"),
    path("create/", CreateStudentView.as_view(), name="create_student"),
    path("update/<uuid:uuid>/", UpdateStudentView.as_view(), name="update_student"),
    path("delete/<uuid:uuid>/", DeleteStudentView.as_view(), name="delete_student"),
]
