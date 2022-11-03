from django.urls import path
from app1 import views

urlpatterns = [
#   Version con vistas normales
#     path('',views.index, name='Inicio'),
#     path('mi_template/',views.mi_template, name='Sobre nosotras'),
#     path('ver_mascota/', views.ver_mascota,name='Ver'),
     path('crear_mascota/',views.crear_mascota,name='Crear'),
#     path('editar_mascota/<int:id>',views.editar_mascota,name='Editar'),
#     path('elimiar_mascota/<int:id>',views.eliminar_mascota,name='Eliminar')

#   Versión con clases basadas en vistas
    path('',views.index, name='Inicio'),
    path('mi_template/',views.mi_template, name='Sobre nosotras'),
    path('ver_mascota/', views.ListaMascotas.as_view(),name='Ver'),
    # path('crear_mascota/',views.CrearMascota.as_view(),name='Crear'),
    path('editar_mascota/<int:pk>',views.EditarMascota.as_view(),name='Editar'),
    path('elimiar_mascota/<int:pk>',views.EliminarMascota.as_view(),name='Eliminar')

]