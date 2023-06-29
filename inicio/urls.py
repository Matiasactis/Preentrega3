from django.contrib import admin
from django.urls import path
from inicio.views import inicio, segunda_vista, fecha_actual, saludar, crear_persona, crear_gato

app_name= 'inicio'

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('admin/', admin.site.urls),
    path('segunda-vista/', segunda_vista, name= 'prueba'),
    path('fecha-actual/', fecha_actual),
    path('saludar/<str:nombre>/<str:apellido>/', saludar ),
    # path('crear-persona/<str:nombre>/<int:edad>/', crear_persona),
    path('crear-persona/', crear_persona, name= 'crear-persona'),
    # path('crear-Pajaro/', crear_pajaro, name= 'crear-pajaro'),
    path('crear-Gato/', crear_gato , name= 'crear-gato'),
]