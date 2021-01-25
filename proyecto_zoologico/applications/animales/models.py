from django.db import models
# IMPORTAR EL MODELO alimentos
from applications.alimentos.models import Alimento
#
from django.contrib.auth.models import User



""" CREAR MODELO raza """
class Raza(models.Model):
    # Atributos del modelo
    raza = models.CharField('raza animal', max_length=50)

    def __str__(self):
        return self.raza





""" CREAR MODELO animales """
class Animales(models.Model):
    # Atributos del modelo
    nombre_animal = models.CharField('nombre animal', max_length=50)
    color = models.CharField('color animal', max_length=50)
    # RELACION AL MODELO Raza
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    # RELACION AL MODELO Alimento
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    # RELACION AL MODELO Usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombre_animal +' '+ self.color +' '+ str(self.raza) +' '+ str(self.alimento) +' '+ str(self.usuario) 
    