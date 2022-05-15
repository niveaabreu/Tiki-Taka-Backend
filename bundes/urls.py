from django.urls import path

from . import views

urlpatterns = [
    path('bundes', views.bundes, name='bundes'),
]