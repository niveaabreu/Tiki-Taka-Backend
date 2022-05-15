from django.urls import path

from . import views

urlpatterns = [
    path('liganos', views.liganos, name='liganos'),
]