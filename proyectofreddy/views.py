from django.shortcuts import render, redirect
from proyectofreddy.models import Paises
from django.db import connection
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request,"Home/home.html")

def mantenimiento_soporte(request):
    return render(request,"Mantenimiento_soporte/mantenimiento_soporte.html")

def reparacion_ardware(request):
    return render(request,"Reparacion_ardware/reparacion_ardware.html")

def seguridad_redes(request):
    return render(request,"Seguridad_redes/seguridad_redes.html")

def administracion_servidores(request):
    return render(request,"Administracion_servidores/administracion_servidores.html")

def nube_virtualizacion(request):
    return render(request,"Nube_virtualizacion/nube_virtualizacion.html")

def desarrollo_it(request):
    return render(request,"Desarrollo_it/desarrollo_it.html")

def telefonia_pbx(request):
    return render(request,"Telefonia_pbx/telefonia_pbx.html")

def servicios_adicionales(request):
    return render(request,"Servicios_adicionales/servicios_adicionales.html")

def contactanos(request):
    return render(request,"Contactanos/contactanos.html")

def nosotros(request):
    return render(request,"Nosotros/nosotros.html")







