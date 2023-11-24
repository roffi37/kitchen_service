from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=False, blank=True)

    def __str__(self) -> str:
        return self.username


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(get_user_model(), related_name="cooks")

    def __str__(self) -> str:
        return self.name
