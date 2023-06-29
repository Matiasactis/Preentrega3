from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    
    
class Gato(models.Model):
    nombre = models.CharField(max_length=24)
    edad = models.IntegerField()

# class Pajaro(models.Model):
#     nombre = models.CharField(max_length=24)
#     edad = models.IntegerField()
