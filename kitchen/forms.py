from django.forms import forms, ModelForm

from kitchen.models import Dish, DishType


class DishCreateForm(ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeCreateForm(ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"
