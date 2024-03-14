from django.db import models
from django.contrib.auth.models import User


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
    watched_time_seconds = models.IntegerField()
    last_watched_time = models.DateTimeField(auto_now=True)

    WATCHED = 'Watched'
    NOT_WATCHED = 'Not Watched'

    STATUS_CHOICES = [
        (WATCHED, 'watched'),
        (NOT_WATCHED, 'not watched'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ['user', 'lesson']

    def save(self, *args, **kwargs):
        if self.watched_time_seconds >= 0.8 * self.lesson.duration_seconds:
            self.status = self.WATCHED
        else:
            self.status = self.NOT_WATCHED
        super(LessonView, self).save(*args, **kwargs)

