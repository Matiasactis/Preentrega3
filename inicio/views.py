from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Persona, Gato, Pajaro
from django.shortcuts import render
from inicio.form import CrearPersonaFormulario, CrearGatoFormulario 

def inicio(request):

    # template = loader.get_template('inicio.html')
    
 
    diccionario = {
        'mensaje' : 'mensaje de inicio'
    }
    
    #contexto = Context (diccionario)
    
    # renderizar_template = template.render(diccionario)
    
    # return HttpResponse (renderizar_template)
    return render(request,'inicio.html')



    

def segunda_vista(request):
    return HttpResponse ('<h2>Segunda vista <h2>')

def fecha_actual(request):
    fecha= datetime.now()
    return HttpResponse (f'<h1>Fecha actual:{fecha}<h1>')

def saludar(request, nombre, apellido):
    return HttpResponse (f'hola! {nombre.title()} {apellido.title()}')





def crear_persona(request):    
    diccionario= {}
    
    if request.method == "POST":
        formulario= CrearPersonaFormulario(request.POST)
        if formulario.is_valid():
            info= formulario.cleaned_data
            persona = Persona(nombre=info ['nombre'] , edad= info ['edad'] )
            persona.save()    
    
            diccionario ['persona']= persona
            
    formulario= CrearPersonaFormulario()
    
    diccionario['formulario'] = formulario
        
    return render(request,'crear-persona.html', diccionario)


def crear_gato(request):    
    if formulariogato == CrearGatoFormulario(request.POST):
        if formulariogato.is_valid():
            data= formulariogato.cleaned_data
            gato= Gato(nombre=data['nombre'], edad = data ['edad'])
            Gato.save()
    formulariogato= CrearGatoFormulario()
    return render (request, 'crear-gato.html', {'formulariogato': formulariogato})