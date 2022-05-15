from django.urls import path

from . import views

urlpatterns = [
    path('laliga', views.laliga, name='laliga'),
]