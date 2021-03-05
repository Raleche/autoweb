from django.contrib import admin
from django.urls import path, include 
from portfolio import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='Contact')
]