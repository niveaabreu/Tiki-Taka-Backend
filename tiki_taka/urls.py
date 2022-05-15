"""tiki_taka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('best_players.urls')),
    path('', include('players.urls')),
    path('', include('golden_boot.urls')),
    path('', include('premier.urls')),
    path('', include('bundes.urls')),
    path('', include('seriea.urls')),
    path('', include('ligue1.urls')),
    path('', include('laliga.urls')),
    path('', include('brasileirao.urls')),
    path('', include('liganos.urls')),
    path('', include('eredvise.urls')),
    path('', include('clubs.urls')),
    path('', include('squads.urls')),
]
