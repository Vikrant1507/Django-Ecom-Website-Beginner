from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About Us"),
    path("contact/", views.contact, name="Contact"),
    path("tracker/", views.tracker, name="Tracker"),
    path("Search/", views.Search, name="Search"),
    path("ProductView/", views.ProductView, name="ProductView"),
    path("checkout/", views.checkout, name="checkout"),
]
