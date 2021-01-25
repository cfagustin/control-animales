

# IMPORTAMOS LOS PAQUETES DE serializes
from rest_framework import serializers
#
from django.contrib.auth.models import User


""" CREAR SERIALIZER UsuarioSerializer """
# serializers :  Heredemos del paquete serializer
# ModelSerializer : Conectando al modelo serializador
class UsuarioSerializer(serializers.ModelSerializer):
    #
    class Meta:
        # Especificar el modelo con el que se va a trabajar
        model = User
        # Especificar los campos que deseamos que serialice en este caso todos
        fields = ('__all__')