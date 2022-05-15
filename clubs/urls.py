from django.urls import path

from . import views

urlpatterns = [
    path('clubs', views.clubs, name='clubs'),
    path('clubs/<int:id>/', views.club),
]