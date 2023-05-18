from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        from core.services.signals import create_user_profile_signal

        post_save.connect(create_user_profile_signal, sender=get_user_model())
