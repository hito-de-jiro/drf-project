from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    watched = models.BooleanField(default=False)
    time_watched = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Product(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item) + ": $" + str(self.price) + " weight: " + str(self.weight) + " kg"
