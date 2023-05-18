from django.urls import path

from core.views import UserLogin, UserLogout, UserRegistration, ActivateUser, UserProfileView
from students.views import search_history

app_name = "core"

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("registration/", UserRegistration.as_view(), name="registration"),
    path("activate/<str:uuid64>/<str:token>/", ActivateUser.as_view(), name="activate_user"),
    path("profile/", UserProfileView.as_view(), name="profile_user"),
    path("history/", search_history, name="history"),
]
