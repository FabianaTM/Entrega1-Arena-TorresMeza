from mailbox import NoSuchMailboxError
from django import forms

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    tipo =forms.CharField(max_length=30)
    edad = forms.IntegerField()

class BusquedaMascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required= False)