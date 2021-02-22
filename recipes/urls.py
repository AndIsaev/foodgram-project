from django.urls import path
from .about import AboutAuthorView, AboutTechView
from . import views, downloads


urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new_recipe, name="new_recipe"),
    path("shop", views.purchase, name="shop"),
    path("favorite/", views.favorites, name="favorites"),
    path("subscription/", views.subscriptions, name="subscriptions"),
    path("<str:username>/", views.profile, name="profile"),
    path("<str:username>/<int:recipe_id>/",
         views.recipe_view, name="recipe_view"),
    path(
        "<str:username>/<int:recipe_id>/edit/",
        views.recipe_edit,
        name="recipe_edit"),
    path(
        "<str:username>/<int:recipe_id>/delete/",
        views.delete_recipe,
        name="delete_recipe"
    ),
    path('purchase/download/', downloads.get_purchase_txt,
         name='get_purchase_txt'),
]

urlpatterns += [
    path('about/author',
         AboutAuthorView.as_view(template_name="about/author.html"),
         name='about_author'),
    path('about/tech',
         AboutTechView.as_view(template_name="about/tech.html"),
         name='about_tech')
]
