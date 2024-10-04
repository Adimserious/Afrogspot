from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=100, blank=False)
    default_email = models.EmailField(blank=False)
    default_phone_number = models.CharField(max_length=15, blank=False)
    default_address_line_1 = models.CharField(max_length=255, blank=False)
    default_address_line_2 = models.CharField(max_length=255,  blank=True, null=True)
    default_city = models.CharField(max_length=100, blank=False)
    default_postal_code = models.CharField(max_length=20, blank=False)
    default_country = CountryField(blank_label='Select a country', blank=False)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        profile = instance.profile
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)