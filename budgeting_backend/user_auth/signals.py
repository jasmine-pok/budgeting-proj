from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from budget.models import Profile
from django.db import transaction

# gets triggered everytime a User is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                Profile.objects.create(user=instance)
        except Exception as e:
            # Log the error and decide whether to re-raise or handle silently
            print(f"Failed to create Profile for user {instance.username}: {e}")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Profile is saved whenever the user is saved
    instance.profile.save()

    