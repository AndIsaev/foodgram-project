from . import views, ajax, downloads, about
from django.urls import path
from .about import AboutAuthorView, AboutTechView

urlpatterns = [

    path("subscription/", views.subscriptions, name="subscriptions"),
    path("favorites", ajax.add_favorites, name="add_favorites"),
    path("favorites/<int:recipe_id>/",
         ajax.remove_favorites, name="remove_favorites"),
    path("ingredients/", ajax.found_ingredient, name="found_ingredient"),
    path("subscriptions", ajax.add_subscription, name="add_subscription"),
    path("subscriptions/<int:author_id>/",
         ajax.remove_subscription, name="remove_subscription"),
    path("purchases", ajax.add_purchases, name="add_purchases"),

    ]

urlpatterns += [
    path("", views.index, name="index"),
    path('purchase/', views.purchase, name='purchase'),
    path('purchase/<int:recipe_id>/',
         views.remove_purchase, name='remove_purchase'),
    path("new", views.new_recipe, name="new_recipe"),
    path("favorite/", views.favorites, name="favorites"),
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
    path('purchase/download/', downloads.get_purchase_txt, name='get_purchase_txt'),
]

urlpatterns += [
    path('about/author', AboutAuthorView.as_view(template_name="author.html"), name='a_author'),
    path('about/tech', AboutTechView.as_view(template_name="tech.html"), name='a_tech')
]