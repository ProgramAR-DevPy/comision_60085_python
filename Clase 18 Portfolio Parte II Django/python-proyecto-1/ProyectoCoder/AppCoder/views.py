from django.shortcuts import render
from models import Curso
from django.http import HttpResponse


# Create your views here.
def curso(self):
    curso = Curso(nombre = "Java", camada = 36589)
    curso.save()

    documento = F"Curso: {curso.nombre} Camada: {curso.camada}   "

    return HttpResponse(documento)