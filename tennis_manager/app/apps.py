from django.apps import AppConfig


class AppConfig(AppConfig):  # noqa: D101
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
