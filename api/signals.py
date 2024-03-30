from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import LessonView


@receiver(pre_save, sender=LessonView)
def update_lesson_view_status(sender, instance, **kwargs):
    """Change status watched for lesson"""
    if instance.time_watched >= 0.8 * instance.lesson.lesson_duration:
        instance.status_watched = True
    else:
        instance.status_watched = False

    instance.last_watched = timezone.localtime()


@receiver(pre_save, sender=LessonView)
def update_lesson_view_time_watched(sender, instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    if instance.time_watched != old_instance.time_watched:
        if instance.time_watched >= instance.lesson.lesson_duration:
            instance.time_watched = instance.lesson.lesson_duration
        elif instance.time_watched < old_instance.time_watched:
            instance.time_watched = old_instance.time_watched
