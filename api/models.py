from django.contrib.auth.models import User
from django.db import models


class Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Product(models.Model):
    owner = models.ForeignKey(Owner, verbose_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    duration = models.IntegerField(default=0)
    time_watched = models.DurationField(blank=True, null=True)
    status_watched = models.BooleanField(default=False)
    last_watched = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    product = models.ManyToManyField(Product, related_name='product_lessons')

    def __str__(self):
        return str(self.title)


class Customer(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    product = models.ForeignKey(Product, verbose_name='product', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.username
