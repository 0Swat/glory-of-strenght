from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('add_attemp/', views.add_attemp),
]