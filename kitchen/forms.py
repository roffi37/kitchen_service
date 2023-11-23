from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms

from kitchen.models import Dish, DishType


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class DishTypeForm(ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class CookForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ("years_of_experience", "username", "first_name", "last_name")
