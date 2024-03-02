from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item) + ": $" + str(self.price) + " weight: " + str(self.weight) + " kg"


