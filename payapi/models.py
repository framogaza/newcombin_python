from pyexpat import model
from django.db import models

class Boleta(models.Model):
    tipo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    fecha = models.DateField()
    importe = models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    estado = models.CharField(max_length=100)
    codigoBarra = models.AutoField(primary_key=True)


