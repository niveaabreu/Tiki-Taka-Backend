from django.urls import path

from . import views

urlpatterns = [
    path('ligue1', views.ligue1, name='ligue1'),
]