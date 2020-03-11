"""profesors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from profesor import views

urlpatterns = [

    #Vistas del proyecto Spring
    path('tablaSpring', views.lol),
    path('deletepas/<int:id>', views.deletepas),
    path('buscar/<int:id>', views.buscar),
    path('act/<int:id>', views.act),
    path('insert', views.insert),
    path('video',views.video),
    path('mapa',views.mapa),
    path('tablaSpring2', views.lol2),
    path('deletepas2/<int:id>', views.deletepas2),
    path('buscar2/<int:id>', views.buscar2),
    path('act2/<int:id>', views.act2),
    path('insert2', views.insert2),

]
