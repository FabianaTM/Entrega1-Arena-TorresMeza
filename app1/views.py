from random import random
import re
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from django.shortcuts import render,redirect
import random

from app1.models import Persona

def hola(request):
    return HttpResponse('Hola')


def mi_template(request):

    cargar_archivo= open(r'C:\Users\fabit\Documents\CoderPython\ProyectoFinal\app1\templates\app1\template.html' ,'r')

    template= Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

def crear_persona(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')

        persona= Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99))
        persona.save()

        return redirect('Ver')

    return render(request,'app1/crear_persona.html',{})

def ver_persona(request):

    personas= Persona.objects.all()

    #template= loader.get_template('ver_persona.html')
    #template_renderizado= template.render({'personas':personas})

    #return HttpResponse(template_renderizado)

    return render(request,'app1/ver_persona.html',{'personas':personas})


def index(request):

    return render(request, 'app1/index.html')