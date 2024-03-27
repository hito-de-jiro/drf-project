from django.db.models.signals import m2m_changed
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


@receiver(m2m_changed, sender=Product.customer.through)
def update_lessons_on_customer_change(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        user_ids = instance.customer.values_list('id', flat=True)
        for user_id in user_ids:
            for lesson in instance.product_lesson.all():
                lesson_view, created = LessonView.objects.get_or_create(user_id=user_id, lesson=lesson)
                if action == 'post_add':
                    lesson_view.status_watched = False
                    lesson_view.time_watched = 0
                    lesson_view.save()
                elif action == 'post_remove':
                    lesson_view.delete()
