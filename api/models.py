from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=255)
    lesson_link = models.URLField()
    lesson_duration = models.IntegerField()

    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.lesson_title


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='lesson', on_delete=models.CASCADE)
    time_watched = models.IntegerField(default=0)
    status_watched = models.BooleanField(default=False)

    last_watched = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lesson']


@receiver(pre_save, sender=LessonView)
def update_lesson_view_status(sender, instance, **kwargs):
    if instance.time_watched >= 0.8 * instance.lesson.lesson_duration:
        instance.status_watched = True
    else:
        instance.status_watched = False

    instance.last_watched = timezone.localtime()
