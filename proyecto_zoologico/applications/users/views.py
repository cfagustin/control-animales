

from django.shortcuts import render
# IMPORTAMOS LAS VISTA GENERICAS DE REST_FRAMEWORK
from rest_framework.generics import ListCreateAPIView 
# IMPORTAR EL SERIALIZER UsuarioSerializer
from .serializers import UsuarioSerializer

#
from django.contrib.auth.models import User
# IMPORTAR PAQUETE DE PERMISION
from applications.permissions import CustomDjangoModelPermissions



""" CREAR VISTA GENERICA DE (usuarios) """
class CrearUsuario(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = UsuarioSerializer

    #
    def get_queryset(self):
        return User.objects.all()
   

