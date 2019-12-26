from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from crum import get_current_request
from ..messaging.email.helpers import send_email

User = get_user_model()


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def warm_user_profile_avatar(sender, **kwargs):
    p = kwargs['instance']
    p.warm_avatar()


def welcome_user(sender, **kwargs):
    print("Send email")
    if kwargs.get('created', False):
        user = kwargs.get('instance', None)

        send_email(
            subject='cambasBlog - Bienvenido a cambasBlog.',
            to_email=[user.email],
            template='emails/welcome.html',
            ctx={
                'user': user.email,
            })
