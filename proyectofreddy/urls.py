"""
URL configuration for proyectofreddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from proyectofreddy.views import home, mantenimiento_soporte, reparacion_ardware, seguridad_redes, administracion_servidores, nube_virtualizacion, desarrollo_it, telefonia_pbx,  servicios_adicionales,  contactanos, nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/home',home),
    path('Mantenimiento_soporte/mantenimiento_soporte',mantenimiento_soporte),
    path('Reparacion_ardware/reparacion_ardware',reparacion_ardware),
    path('Seguridad_redes/seguridad_redes',seguridad_redes),
    path('Administracion_servidores/administracion_servidores',administracion_servidores),
    path('Nube_virtualizacion/nube_virtualizacion',nube_virtualizacion),
    path('Desarrollo_it/desarrollo_it',desarrollo_it),
    path('Telefonia_pbx/telefonia_pbx',telefonia_pbx),
    path('Servicios_adicionales/servicios_adicionales',servicios_adicionales),
    path('Contactanos/contactanos',contactanos),
    path('Nosotros/nosotros',nosotros),



]
