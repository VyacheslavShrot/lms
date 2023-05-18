from django.contrib import messages
from django.contrib.auth import login, get_user_model

from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from django.views.generic import TemplateView, CreateView, RedirectView

from core.forms import UserRegistrationForm
from core.models import UserProfile

from core.services.emails import send_registration_email
from core.utils.token_generator import TokenGenerator


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        print(f"In view {request.current_time}")
        if request.user.is_authenticated:
            messages.success(request, "User is available")
        else:
            messages.info(request, "Please login")

        return super().get(self, request, *args, **kwargs)


class UserLogin(LoginView):
    ...


class UserLogout(LogoutView):
    ...


class UserRegistration(CreateView):
    template_name = "registration/create_user.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        send_registration_email(request=self.request, user_instance=self.object)

        return super().form_valid(form)


class ActivateUser(RedirectView):
    url = reverse_lazy("index")

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (ValueError, get_user_model().DoesNotExist, TypeError):
            return render(request, template_name="404.html")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()

            login(request, current_user)
            return super().get(request, *args, **kwargs)

        return render(request, template_name="404.html")


class UserProfileView(TemplateView):
    model = UserProfile
    template_name = "user/profile.html"
