from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("success_reg", views.success_reg, name="success_reg")
    ]
