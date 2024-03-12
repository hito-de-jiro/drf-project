from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    owner = models.ForeignKey(User, verbose_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    duration = models.IntegerField(default=0)

    product = models.ManyToManyField(Product, related_name='products_lessons')

    def __str__(self):
        return str(self.title)


class UserLesson(models.Model):
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.PROTECT)
    lesson = models.ForeignKey(Lesson, verbose_name='lesson', related_name='lessons', on_delete=models.PROTECT)

    time_watched = models.DurationField(blank=True, null=True, default=0)
    status_watched = models.BooleanField(default=False)

    last_watched = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '%d: %s' % (self.user, self.lesson)
