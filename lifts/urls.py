from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_attempt, name='add_attempt'),
    path('<int:pk>/', views.attempt_detail, name='attempt_detail'),
    path('<int:pk>/delete/', views.attempt_delete, name='attempt_delete'),
]
