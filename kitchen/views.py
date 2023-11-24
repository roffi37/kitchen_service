from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm, DishTypeForm, CookForm, CookCreationForm
from kitchen.models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    num_cooks = get_user_model().objects.count()
    num_dish = Dish.objects.count()
    num_dish_type = DishType.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_dish": num_dish,
        "num_dish_type": num_dish_type,
    }
    return render(request, "kitchen/index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    context_object_name = "dish_list"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")
    form_class = DishForm
    context_object_name = "dish_create"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")
    context_object_name = "dish-delete"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")
    form_class = DishForm
    context_object_name = "dish-update"


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    form_class = DishTypeForm
    context_object_name = "dish_type_create"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    form_class = DishTypeForm
    context_object_name = "dish-type-delete"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    form_class = DishTypeForm
    context_object_name = "dish-type-update"


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    context_object_name = "cook-delete"
    form_class = CookForm


class CookCreateView(generic.CreateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    context_object_name = "cook-create"
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    form_class = CookForm
    context_object_name = "user-create"
