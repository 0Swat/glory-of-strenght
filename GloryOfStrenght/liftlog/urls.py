from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('upload/', views.upload_video, name='upload'),
]
