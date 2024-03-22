from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import LessonView, Product


@receiver(pre_save, sender=LessonView)
def update_lesson_view_status(sender, instance, **kwargs):
    """Change status watched for lesson"""
    if instance.time_watched >= 0.8 * instance.lesson.lesson_duration:
        instance.status_watched = True
    else:
        instance.status_watched = False

    instance.last_watched = timezone.localtime()


@receiver(post_save, sender=Product)
def update_lessons(sender, instance, created, **kwargs):
    """Update data watched lesson"""
    if created:
        user = instance.customer
        lessons = instance.lesson_set.all()

        for lesson in lessons:
            LessonView.objects.get_or_create(user=user, lesson=lesson)
