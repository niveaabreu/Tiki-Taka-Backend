from django.urls import path

from . import views

urlpatterns = [
    path('golden', views.golden, name='golden'),

]