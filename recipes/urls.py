from django.urls import path, include
from . import views, ajax

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new_recipe, name="new_recipe"),
    path("favorite/", views.favorites, name="favorites"),
    path('favorites', ajax.add_favorites, name='add_favorites'),
    path('favorites/<int:recipe_id>/',
         ajax.remove_favorites, name='remove_favorites'),
    path('ingredients/', ajax.found_ingredient, name='found_ingredient'),
    path("<str:username>/", views.profile, name="profile"),
    path("<str:username>/<int:recipe_id>/", views.recipe_view, name="recipe_view"),
    path(
        "<str:username>/<int:recipe_id>/edit/",
        views.recipe_edit,
        name="recipe_edit"),
    path(
        "<str:username>/<int:recipe_id>/delete/",
        views.delete_recipe,
        name="delete_recipe"
    ),
    ]

