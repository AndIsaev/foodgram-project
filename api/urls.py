from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api import ajax
from api.views import PurchaseViewSet


router = DefaultRouter()
router.register(r'purchases', PurchaseViewSet, basename='purchases'),


urlpatterns = [
    path('', include(router.urls)),
    path("favorites", ajax.add_favorites, name="add_favorites"),
    path("favorites/<int:recipe_id>/",
         ajax.remove_favorites, name="remove_favorites"),
    path("ingredients/", ajax.found_ingredient, name="found_ingredient"),
    path("subscriptions", ajax.add_subscription, name="add_subscription"),
    path("subscriptions/<int:author_id>/",
         ajax.remove_subscription, name="remove_subscription"),
]
