from random import random
import re
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from django.shortcuts import render,redirect
import random
from app1.forms import BusquedaMascotaFormulario, MascotaFormulario
import os

from app1.models import Mascota

def mi_template(request):
    cargar_archivo= open(r'.\app1\templates\app1\template.html' ,'r')

    template= Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

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
    print(nombre)

    if nombre:
        mascotas = Mascota.objects.filter(nombre__icontains=nombre)
        print(mascotas)
    else:
        mascotas = Mascota.objects.all
    print(mascotas)
    print('///////////////////////////////////////////////')
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

    return render(request,'app1/editar_mascota.html',{'formulario': formulario}) 