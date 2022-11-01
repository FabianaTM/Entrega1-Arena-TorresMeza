from mailbox import NoSuchMailboxError
from django import forms
from datetime import datetime

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    tipo =forms.CharField(max_length=30)
    edad = forms.IntegerField()
    #fecha_publicacion= forms.DateField()

class BusquedaMascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required= False)