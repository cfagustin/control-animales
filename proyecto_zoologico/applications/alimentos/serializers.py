# IMPORTAR LOS PAQUETES SERIALIZERS
from rest_framework import serializers
# IMPORTAR EL MODELO Alimento
from .models import Alimento, Tipo
#
from django.contrib.auth.models import User




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





""" CREAR SERIALIZER Listar Alimento """
class AlimentoListarSerializer(serializers.ModelSerializer):

    # Redefinir con el serializador
    tipo_alimento = TipoSerializer() 
    usuario = UsuarioSerializer()
    
    class Meta:
        model = Alimento
        fields = (
            'id',
            'nombre_alimento',
            'tipo_alimento',
            'cantidad',
            'usuario',
        )




""" CREAR SERIALIZER Alimento"""
class AlimentoSerializer(serializers.ModelSerializer):

    class Meta:
        # Especificar el modelo con que se va a trabajar
        model = Alimento
        # Especificar los campos que deseemos que serialice en este caso todos
        fields = ('__all__')





    