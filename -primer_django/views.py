from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Persona
#v1
#def inicio(request):
#    return HttpResponse ('Inicio')

#v2

#def inicio(request):
#    archivo = open(r'C:\Users\matia\Desktop\python\templates\inicio.html', 'r')
    
    #emplate = Template(archivo.read())
    
#    archivo.close()
    
    #diccionario = {
     #   'mensaje' : 'mensaje de inicio'
    #}
    
   # contexto = Context (diccionario)
    
   # renderizar_template = template.render(contexto)
    
   # return HttpResponse (renderizar_template)

#v3
def inicio(request):

    template = loader.get_template('inicio.html')
    
 
    diccionario = {
        'mensaje' : 'mensaje de inicio'
    }
    
    #contexto = Context (diccionario)
    
    renderizar_template = template.render(diccionario)
    
    return HttpResponse (renderizar_template)


    

def segunda_vista(request):
    return HttpResponse ('<h2>Segunda vista <h2>')

def fecha_actual(request):
    fecha= datetime.now()
    return HttpResponse (f'<h1>Fecha actual:{fecha}<h1>')

def saludar(request, nombre, apellido):
    return HttpResponse (f'hola! {nombre.title()} {apellido.title()}')


def crear_persona(request, nombre, edad):
    template = loader.get_template('crear-persona.html')
    persona = Persona(nombre=nombre, edad=edad)
    persona.save()    
    
    diccionario = {
        'persona': Persona
    }

    renderizar_template = template.render(diccionario)
    return HttpResponse (renderizar_template)
