from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    DishTypeDetailView,
    DishTypeListView,
    DishTypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dishes-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]

app_name = "kitchen"
