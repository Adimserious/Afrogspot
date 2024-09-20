from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Create or get profile when a user is created
    Profile.objects.get_or_create(user=instance)

    # save the profile if user already exists (to ensure updates)
    instance.profile.save()

    # Logging for debugging
    if created:
        logger.info(f"Profile created for user {instance.username}")
    else:
        logger.info(f"Profile updated for user {instance.username}")
