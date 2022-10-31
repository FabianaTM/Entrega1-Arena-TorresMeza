from contextlib import nullcontext
from datetime import datetime
from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class Mascota(models.Model):
    nombre= models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_publicacion=models.DateTimeField(default= datetime.now())

    def __str__(self):
        return f'Nombre:{self.nombre} - Tipo:{self.tipo}'
    