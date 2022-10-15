from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from django.shortcuts import render


from app1.models import Persona

def hola(request):
    return HttpResponse('Hola')


def mi_template(request):

    cargar_archivo= open(r'C:\Users\fabit\Documents\CoderPython\ProyectoFinal\templates\template.html' ,'r')

    template= Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

def crear_persona(request, nombre, apellido, edad):

    persona= Persona(nombre=nombre, apellido=apellido, edad=edad)
    persona.save()

    template= loader.get_template('crear_persona.html')
    template_renderizado= template.render({'persona':persona})

    return HttpResponse(template_renderizado)


def ver_persona(request):

    personas= Persona.objects.all()

    template= loader.get_template('ver_persona.html')
    template_renderizado= template.render({'personas':personas})

    return HttpResponse(template_renderizado)