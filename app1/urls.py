from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index, name='Inicio'),
    path('mi_template/',views.mi_template, name='Sobre nosotras'),
    path('ver_mascota/', views.ver_mascota,name='Ver'),
    path('crear_mascota/',views.crear_mascota,name='Crear'),
    path('editar_mascota/',views.editar_mascota,name='Editar')
    #path('elimiar_mascota/',views.eliminar_mascota,name='Eliminar')
]