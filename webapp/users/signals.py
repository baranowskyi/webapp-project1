from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import UserSite

from rest_framework.authtoken.models import Token

# create token authentication after create user
@receiver(post_save, sender=UserSite)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)