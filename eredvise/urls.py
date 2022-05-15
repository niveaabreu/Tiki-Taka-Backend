from django.urls import path

from . import views

urlpatterns = [
    path('eredvise', views.eredvise, name='eredvise'),
]