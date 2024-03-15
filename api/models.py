from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()

    products = models.ManyToManyField(Product)


class LessonView(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='lesson', on_delete=models.CASCADE)
    watched_time_seconds = models.IntegerField(default=0)
    last_watched_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,  default='Not Watched')

    class Meta:
        unique_together = ['user', 'lesson']


@receiver(post_save, sender=LessonView)
def update_lesson_view_status(sender, instance, **kwargs):
    if instance.watched_time_seconds >= 0.8 * instance.lesson.duration_seconds:
        instance.status = 'Watched'
    else:
        instance.status = 'Not Watched'
    instance.save()