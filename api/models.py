from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Lesson(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField()
    duration = models.IntegerField()
    time_watched = models.DurationField(blank=True, null=True)
    status_watched = models.BooleanField(default=False)
    product = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return str(self.title)


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    lessons = models.ManyToManyField(Lesson, related_name='watched_lessons', blank=True)

    def __str__(self):
        return self.username
