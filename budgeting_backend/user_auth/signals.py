from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from budget.models import Profile

# gets triggered everytime a User is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Profile is saved whenever the user is saved
    instance.profile.save()

    