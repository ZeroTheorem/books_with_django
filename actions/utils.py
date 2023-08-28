import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action


def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.datetime.now()

    simular_action = Action.objects.filter(
        user=user, verb=verb, created__gte=last_minute
    )

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        simular_action = simular_action.filter(target_ct=target_ct, target_id=target.id)

    if not simular_action:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False
