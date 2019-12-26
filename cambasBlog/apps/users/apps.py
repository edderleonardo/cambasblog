from django.db.models.signals import post_save
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'cambasBlog.apps.users'
    label = 'cambasBlog_users'
    verbose_name = 'User'

    def ready(self):
        from django.contrib.auth import get_user_model
        from cambasBlog.apps.users.signals import (
            create_auth_token, warm_user_profile_avatar, welcome_user)
        user = get_user_model()
        post_save.connect(create_auth_token, sender=user)
        post_save.connect(warm_user_profile_avatar, sender=user)
        post_save.connect(welcome_user, sender=user)
