from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

from kitchen.models import Dish, DishType, Cook


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
        fields = ("years_of_experience", "first_name", "last_name")


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("years_of_experience", )
