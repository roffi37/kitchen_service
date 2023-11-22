from django.forms import ModelForm

from kitchen.models import Dish, DishType


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeForm(ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"
