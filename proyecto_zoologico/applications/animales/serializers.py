
# IMPORTAR LOS PAQUETES SERIALIZERS
from rest_framework import serializers
# IMPORTAR EL MODELO Alimento
from .models import Animales, Raza, Alimento
#
from django.contrib.auth.models import User
# IMPORTAR EL MODELO Tipo 
from applications.alimentos.models import Tipo





""" CREAR SERIALIZER Raza"""
class RazaSerializer(serializers.ModelSerializer):

    class Meta:
        # Especificar el modelo con que se va a trabajar
        model = Raza
        # Especificar los campos que deseemos que serialice en este caso todos
        fields = ('__all__')



""" CREAR SERIALIZER Tipo"""
class TipoSerializer(serializers.ModelSerializer):

    class Meta:
        # Especificar el modelo con que se va a trabajar
        model = Tipo
        # Especificar los campos que deseemos que serialice en este caso todos
        fields = ('__all__')



""" CREAR SERIALIZER Usuario"""
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        # Especificar el modelo con que se va a trabajar
        model = User
        # Especificar los campos que deseemos que serialice en este caso todos
        fields = ('__all__')




""" CREAR SERIALIZER ALimento"""
class AlimentoSerializer(serializers.ModelSerializer):

    # Redefinir con el serializador
    tipo_alimento = TipoSerializer()
    usuario = UsuarioSerializer()

    class Meta:
        # Especificar el modelo con que se va a trabajar
        model = Alimento
        # Especificar los campos que deseemos que serialice en este caso todos
        fields = (
            'id',
            'nombre_alimento',
            'tipo_alimento',
            'cantidad',
            'usuario',
        )






""" CREAR SERIALIZER Listar Animal """
class AnimalListarSerializer(serializers.ModelSerializer):

    # Redefinir con el serializador
    raza = RazaSerializer() 
    alimento = AlimentoSerializer()
    usuario = UsuarioSerializer()
    
    class Meta:
        model = Animales
        fields = (
            'id',
            'nombre_animal',
            'color',
            'raza',
            'alimento',
            'usuario',
        )



""" CREAR SERIALIZER Animal"""
class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        # Especificar el modelo con que se va a trabajar
        model = Animales
        # Especificar los campos que deseemos que serialice en este caso todos
        fields = ('__all__')



