from datetime import datetime
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from django.shortcuts import render,redirect
from app1.forms import BusquedaMascotaFormulario, MascotaFormulario
import os

from app1.models import Mascota

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def mi_template(request):
    cargar_archivo= open(r'.\app1\templates\app1\template.html' ,'r')

    template= Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

@login_required
def crear_mascota(request):
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():

            data= formulario.cleaned_data

            nombre = data['nombre']
            tipo = data['tipo']
            edad = data['edad']
            
            mascota= Mascota(nombre=nombre, tipo=tipo, edad=edad)
            mascota.save()

            return redirect('Ver')
        
        else:
             return render(request,'app1/crear_mascota.html',{'formulario': formulario})
    
    formulario = MascotaFormulario()

    return render(request,'app1/crear_mascota.html',{'formulario': formulario})


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

def editar_mascota (request,id):
    mascota= Mascota.objects.get(id=id)
    if request.method == 'POST':
        
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():

            data= formulario.cleaned_data

            mascota.nombre= data['nombre']
            mascota.tipo= data['tipo']
            mascota.edad=data['edad']
            mascota.save()

            return redirect('Ver')
        
    formulario = MascotaFormulario(initial={'nombre':mascota.nombre,'tipo':mascota.tipo,'edad':mascota.edad})

    return render(request,'app1/editar_mascota.html',{'formulario': formulario, 'mascota': mascota})


def eliminar_mascota (request,id):
    mascota= Mascota.objects.get(id=id)
    mascota.delete()
    return redirect ('Ver')


class ListaMascotas(ListView):
    model= Mascota
    template_name= 'app1/ver_mascota_cbv.html'

class CrearMascota(CreateView):
    model= Mascota
    success_url = '/ver_mascota/'
    template_name= 'app1/crear_mascota_cbv.html'
    fields = ['nombre','tipo','edad']

class EditarMascota(LoginRequiredMixin ,UpdateView):
    model= Mascota
    success_url = '/ver_mascota/'
    template_name= 'app1/editar_mascota_cbv.html'
    fields = ['nombre','tipo','edad']

class EliminarMascota(LoginRequiredMixin,DeleteView):
    model= Mascota
    success_url = '/ver_mascota/'
    template_name= 'app1/eliminar_mascota_cbv.html'


# class VerMascota():