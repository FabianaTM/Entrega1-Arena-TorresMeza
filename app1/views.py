from datetime import datetime
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from django.shortcuts import render,redirect
from app1.forms import BusquedaMascotaFormulario, MascotaFormulario
import os

from app1.models import Mascota

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#Vistas normales:

def mi_template(request):
    cargar_archivo= open(r'.\app1\templates\app1\template.html' ,'r')

    template= Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)


def ver_mascota(request):
    nombre =request.GET.get('nombre')
    if nombre:
        mascotas = Mascota.objects.filter(nombre__icontains=nombre)
    else:
        mascotas = Mascota.objects.all()
    formulario= BusquedaMascotaFormulario()

    return render(request,'app1/ver_mascota.html',{'mascotas':mascotas, 'formulario':formulario})


def index(request):
    return render(request, 'app1/index.html')


# Clases basadas en vistas:

class CrearMascota(LoginRequiredMixin,CreateView):
    model= Mascota
    success_url = '/ver_mascota/'
    template_name= 'app1/crear_mascota_cbv.html'
    fields = ['nombre','tipo','edad','fecha_publicacion','descripcion']

class EditarMascota(LoginRequiredMixin ,UpdateView):
    model= Mascota
    success_url = '/ver_mascota/'
    template_name= 'app1/editar_mascota_cbv.html'
    fields = ['nombre','tipo','edad','fecha_publicacion','descripcion']

class EliminarMascota(LoginRequiredMixin,DeleteView):
    model= Mascota
    success_url = '/ver_mascota/'
    template_name= 'app1/eliminar_mascota_cbv.html'


class VerMascota(DetailView):
    model= Mascota
    template_name= 'app1/mascota.html'