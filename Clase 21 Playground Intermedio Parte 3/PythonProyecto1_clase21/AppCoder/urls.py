from django.urls import path
from AppCoder import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),  #Le damos un nuevo argumento, indicando el nombre de la vista. para que al tocar cada boton, django sepa a donde ir.
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    path('curso-form/', views.curso_form, name='CursoForm'),
    path('curso-form-2/', views.curso_form_2, name='CursoForm2'),
    path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    
]
