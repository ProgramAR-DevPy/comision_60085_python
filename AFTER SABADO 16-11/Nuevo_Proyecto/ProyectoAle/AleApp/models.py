from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length= 30)
    camada = models.IntegerField()

class Productos(models.Model):
    nombre = models.CharField(max_length= 30)
    sku = models.IntegerField()