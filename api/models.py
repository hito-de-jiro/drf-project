from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    duration = models.IntegerField()
    time_watched = models.DurationField(blank=True, null=True)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.title)
