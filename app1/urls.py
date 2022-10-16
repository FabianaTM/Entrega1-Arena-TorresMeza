from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index, name='Inicio'),
    #path('hola/', views.hola, name='Saludo'),
    path('mi_template/',views.mi_template, name='Sobre nosotras'),
    path('ver_persona/', views.ver_persona,name='Ver'),
    path('crear_persona/',views.crear_persona,name='Crear'),
]