from mailbox import NoSuchMailboxError
from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_lenght=30)
    apellido =forms.CharField(max_lenght=30)
    edad = forms.IntegerField()