from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=24)
    edad = models.models.IntegerField()
    
class Gato(models.Model):
    nombre = models.CharField(max_length=24)
    edad = models.IntegerField()

class Pajaro(models.Model):
    nombre = models.CharField(max_length=24)
    edad = models.IntegerField()