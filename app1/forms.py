from mailbox import NoSuchMailboxError
from django import forms
from datetime import datetime
from ckeditor.fields import RichTextFormField

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    tipo =forms.CharField(max_length=30)
    edad = forms.IntegerField()
    descripcion= RichTextFormField(required=True)
    fecha_publicacion= forms.DateField(required=False)

class BusquedaMascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required= False)