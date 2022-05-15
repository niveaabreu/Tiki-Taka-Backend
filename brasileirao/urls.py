from django.urls import path

from . import views

urlpatterns = [
    path('brasileirao', views.brasileirao, name='brasileirao'),
]