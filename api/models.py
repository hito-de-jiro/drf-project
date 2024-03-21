from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ManyToManyField(User, related_name='product_customer')

    def __str__(self):
        return self.product_name


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
