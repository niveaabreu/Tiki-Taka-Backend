from django.urls import path

from . import views

urlpatterns = [
    path('/', views.best),
    path('best', views.best, name='best'),

]