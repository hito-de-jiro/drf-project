from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()

    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='lesson', on_delete=models.CASCADE)
    watched_time_seconds = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    last_watched_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lesson']


@receiver(pre_save, sender=LessonView)
def update_lesson_view_status(sender, instance, **kwargs):
    if instance.watched_time_seconds >= 0.8 * instance.lesson.duration_seconds:
        instance.status = True
    else:
        instance.status = False

    instance.last_watched_time = timezone.localtime()
