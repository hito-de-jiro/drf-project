from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    duration = models.IntegerField()

    product = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.title)


class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    time_watched = models.IntegerField()
    WATCHED = 'Watched'
    NOT_WATCHED = 'Not Watched'

    STATUS_CHOICES = [
        (WATCHED, 'watched'),
        (NOT_WATCHED, 'not watched'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    last_watched = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.time_watched >= 0.8 * self.lesson.duration:
            self.status = self.WATCHED
        else:
            self.status = self.NOT_WATCHED
        super(UserLesson, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.lesson)
