from django.shortcuts import render
# IMPORTAR EL MODELO Alimento
from .models import Alimento, Tipo
# IMPORTAR EL PAQUETE DE CreatApiView
from rest_framework.generics import(
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

# IMPORTAR EL SERIALIZER
from .serializers import(
    TipoSerializer,
    AlimentoListarSerializer,
    AlimentoSerializer,
)
#
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
# IMPORTAR PAQUETE DE PERMISION
from applications.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import IsAuthenticated
#
from django.db.models import Avg




""" CREAR VISTA PARA REGISTRAR (alimentos) """
class CrearTipoAlimento(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = TipoSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Tipo.objects.all()



###################################################################




""" CREAR VISTA PARA LISTAR (alimentos) """
class ListarAlimentos(ListAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AlimentoListarSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Alimento.objects.all()




""" CREAR VISTA PARA REGISTRAR (alimentos) """
class CrearAlimento(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AlimentoSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Alimento.objects.all()



""" CREAR VISTA PARA ACTUALIZAR (alimentos) """
class ActualizarAlimento(RetrieveUpdateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AlimentoSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Alimento.objects.all()




""" CREAR VISTA PARA ELIMINAR (alimentos) """
class EliminarAlimento(DestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    # Indicamos bajo que serializador deseamos realizar el registro
    serializer_class = AlimentoSerializer

    # Definir la consulta a la base de datos
    def get_queryset(self):
        return Alimento.objects.all()



