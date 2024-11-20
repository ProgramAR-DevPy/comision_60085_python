from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario

# Create your views here.
def inicio(req):
    return render(req, 'appcoder/padre.html')


def cursos(req):
    return render(req, 'appcoder/cursos.html')

def profesores(req):
    return render(req, 'appcoder/profesores.html')

def estudiantes(req):
    return render(req, 'appcoder/estudiantes.html')

def entregables(req):
    return render(req, 'appcoder/entregables.html')


def curso_form(req):
    if req.method == 'POST':
      
            curso =  Curso(nombre=req.POST['curso'],camada=req.POST['camada'])
 
            curso.save()
 
            return render(req, "AppCoder/index.html")
 
    return render(req,"AppCoder/curso_formulario.html")

def curso_form_2(request):

    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = CursoFormulario(request.POST)  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])  # Creamos un objeto Curso
            curso.save()  # Guardamos el curso en la base de datos
            return render(request, "AppCoder/index.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = CursoFormulario()  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(request, "AppCoder/curso_formulario_2.html", {"miFormulario": miFormulario})


def busquedaCamada(request):
     return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["camada"]:

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']

        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:

        respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)