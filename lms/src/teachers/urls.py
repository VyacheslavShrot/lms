from django.urls import path

from teachers.views import CreateTeacherView, UpdateTeacherView, DeleteTeacherView, GetTeacherView

app_name = "teachers"

urlpatterns = [
    path("", GetTeacherView.as_view(), name="get_teachers"),
    path("create/", CreateTeacherView.as_view(), name="create_teacher"),
    path("update/<int:pk>/", UpdateTeacherView.as_view(), name="update_teacher"),
    path("delete/<int:pk>/", DeleteTeacherView.as_view(), name="delete_teacher"),
]
