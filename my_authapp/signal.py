from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import CastomUser


@receiver(m2m_changed, sender=CastomUser.following.through)
def user_following_change(sender, instance, **kwargs):
    instance.count_following = instance.following.count()
    instance.save()
