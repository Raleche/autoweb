from django.contrib import admin
from django.urls import path, include 
from . import views

app_name = "fixweb"

# Django admin header customization

admin.site.site_header = "Auto & Fix Mechanical Breakdown System"
admin.site.site_title = "Welcome Auto & Fix system"
admin.site.index_title = "Auto & Fix Portal"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("products", views.products, name="products"),
    path("contact", views.contact, name="contact")
]