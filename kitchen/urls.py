from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishDeleteView,
    DishUpdateView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookDeleteView,
    CookUpdateView,
    DishTypeDetailView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dishes-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dishes-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes-types/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes-types/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
]

app_name = "kitchen"
