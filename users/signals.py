from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
    # print("Profile Saved!")
    # print("Sender:", sender)
    # print("Instance:", instance)
    # print("Created:", created)


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created is False:
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
