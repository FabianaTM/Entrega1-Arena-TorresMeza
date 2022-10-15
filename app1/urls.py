from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index),
    path('hola/', views.hola),
    path('mi_template/',views.mi_template),
    path('ver_persona/', views.ver_persona),
    path('crear_persona/<str:nombre>/<str:apellido>/<int:edad>/',views.crear_persona),
]