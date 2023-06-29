from django.contrib import admin
from inicio.models import Persona, Gato, Pajaro
# Register your models here.

# ACA registras LOS MODELOS (clases creadas en models.py)
admin.site.register(Persona)
admin.site.register(Gato)
admin.site.register(Pajaro)