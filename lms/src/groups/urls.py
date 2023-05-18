from django.urls import path

from groups.views import GetGroupView, CreateGroupView, UpdateGroupView, DeleteGroupView, GetGroupsTeachersView

app_name = "groups"

urlpatterns = [
    path("", GetGroupView.as_view(), name="get_groups"),
    path("create/", CreateGroupView.as_view(), name="create_group"),
    path("update/<int:pk>/", UpdateGroupView.as_view(), name="update_group"),
    path("delete/<int:pk>/", DeleteGroupView.as_view(), name="delete_group"),
    path("get-groups-teachers/<int:pk>/", GetGroupsTeachersView.as_view(), name="get_groups_teachers"),
]
