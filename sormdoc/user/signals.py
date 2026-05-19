from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, created, **kwargs):
    # Profile.save() calls user.save(update_fields=['first_name', 'last_name']) to
    # persist property changes. Skip re-saving the profile in that case to avoid
    # infinite recursion: user.save → signal → profile.save → user.save → …
    update_fields = kwargs.get('update_fields')
    if update_fields and set(update_fields) <= {'first_name', 'last_name'}:
        return
    if not created and hasattr(instance, 'profile'):
        instance.profile.save()
