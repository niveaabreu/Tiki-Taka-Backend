from django.urls import path

from . import views

urlpatterns = [
    path('squads/<int:id>/', views.squads),
]