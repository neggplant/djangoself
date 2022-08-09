from django.apps import AppConfig
from django.core.signals import request_finished


class AppdjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.djapp'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from application.utils.signals import my_callback
        # Explicitly connect a signal handler.
        request_finished.connect(my_callback)