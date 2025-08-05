from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=SocialAccount)
def update_user_social_info(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.social_provider = instance.provider
        user.can_change_username = True
        user.save()