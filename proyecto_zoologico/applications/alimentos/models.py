
from django.db import models
# IMPORTAR EL MODELO usuarios
#from applications.users.models import Usuario
#
from django.contrib.auth.models import User


""" CREAR EL MODELO tipo_alimento """
class Tipo(models.Model):
    tipo = models.CharField('tipo alimento', max_length=50)

    def __str__(self):
        return self.tipo




""" CREAR EL MODELO alimentos """
class Alimento(models.Model):

    # Atributos para el modelo alimentos
    nombre_alimento = models.CharField('nombre alimento', max_length=50)
    tipo_alimento = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad')

    # RELACION DE LLAVE FORANEA 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    # Definir una funcion que retorna ciertos valores a mostrar
    def __str__(self):
        return self.nombre_alimento 






    