"""
URL configuration for EmpresaMA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ma_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('registro/', views.registro_view, name='nombre_de_tu_vista_registro'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('empleados/', views.empleados, name='empleados'),
    path('inventario/', views.inventario, name='inventario'),
    path('ver_cotizacion/', views.ver_cotizacion, name='ver_cotizacion'),
]
