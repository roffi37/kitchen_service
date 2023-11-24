from django.contrib import admin
from django.contrib.auth import get_user_model

from kitchen.models import DishType, Dish

admin.site.register(get_user_model())
admin.site.register(DishType)
admin.site.register(Dish)
