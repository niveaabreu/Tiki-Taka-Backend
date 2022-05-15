from django.urls import path

from . import views

urlpatterns = [
    path('seriea', views.seriea, name='seriea'),
]