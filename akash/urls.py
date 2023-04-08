
from django.contrib import admin
from django.urls import path
from akash import views

urlpatterns = [
    path('', views.index),
    path("cart/", views.cart, name="cart"),
    path("login/", views.login, name="login"),
    path("searchmed/", views.searchmed, name="searchmed"),
    path("signup/", views.signup, name="signup"),
    path("ordercomplete/", views.ordercomplete, name="ordercomplete"),

]
