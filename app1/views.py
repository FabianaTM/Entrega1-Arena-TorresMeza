from random import random
import re
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from django.shortcuts import render,redirect
import random
from app1.forms import BusquedaPersonaFormulario, PersonaFormulario
import os

from app1.models import Persona

def hola(request):
    return HttpResponse('Hola')


def mi_template(request):
    cargar_archivo= open(r'.\app1\templates\app1\template.html' ,'r')

    template= Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

def crear_persona(request):

    if request.method == 'POST':

        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():

            data= formulario.cleaned_data

            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']

            persona= Persona(nombre=nombre, apellido=apellido, edad=edad)
            persona.save()

            return redirect('Ver')
        
        else:
             return render(request,'app1/crear_persona.html',{'formulario': formulario})
    
    formulario = PersonaFormulario()

    return render(request,'app1/crear_persona.html',{'formulario': formulario})

def ver_persona(request):

    nombre =request.GET.get('nombre')
    print(nombre)

    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
        print(personas)
    else:
        personas = Persona.objects.all

    formulario= BusquedaPersonaFormulario()

    return render(request,'app1/ver_persona.html',{'personas':personas, 'formulario':formulario})


def index(request):

    return render(request, 'app1/index.html')

def editar_persona (request,id):
    persona= Persona.objects.get(id=id)
    if request.method == 'POST':

        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():

            data= formulario.cleaned_data

            persona.nombre= data['nombre']
            persona.apellido= data['apellido']
            persona.edad=data['edad']

            persona.save()

            return redirect('Ver')
        
    
    formulario = PersonaFormulario(initial={'nombre':persona.nombre,'apellido':persona.apellido,'edad':persona.edad})

    return render(request,'app1/editar_persona.html',{'formulario': formulario}) 