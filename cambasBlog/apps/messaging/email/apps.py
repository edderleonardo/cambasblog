from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'cambasBlog.apps.messaging.email'
    label = 'cambasBlog_email'

    def ready(self):
        pass
