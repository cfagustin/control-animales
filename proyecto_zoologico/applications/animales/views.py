from django.shortcuts import render
# IMPORTAR MODELO animales
from .models import Alimento, Raza, Animales
# IMPORTAR VISTAS GENERICAS
from rest_framework.generics import(
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
# IMPORTAR EL SERIALIZER
from .serializers import(
    RazaSerializer,
    AnimalSerializer,
    AnimalListarSerializer,
)

# IMPORTAR PAQUETE DE PERMISION
from applications.permissions import CustomDjangoModelPermissions





""" CREAR VISTA PARA REGISTRAR (raza) """
class CrearRaza(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = RazaSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Raza.objects.all()
    

###############################################################

""" CREAR VISTA PARA LISTAR (animales) """
class ListarAnimales(ListAPIView):

    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AnimalListarSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Animales.objects.all()





""" CREAR VISTA PARA REGISTRAR (animales) """
class CrearAnimal(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)

    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AnimalSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Animales.objects.all()




""" CREAR VISTA PARA ACTUALIZAR (animales) """
class ActualizarAnimal(RetrieveUpdateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AnimalSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Animales.objects.all()



""" CREAR VISTA PARA ELIMINAR (animales) """
class EliminarAnimal(DestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AnimalSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Animales.objects.all()



