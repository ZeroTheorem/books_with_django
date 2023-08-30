from django.apps import AppConfig


class MyAuthappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_authapp"

    def ready(self):
        import my_authapp.signal
