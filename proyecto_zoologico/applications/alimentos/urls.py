from django.contrib import admin
from django.urls import path

# IMPORTAMOS LAS VISTAS GENERICAS
from . import views


urlpatterns = [
    path(
        'api/tipo/crear',
        views.CrearTipoAlimento.as_view(),
    ),
    path(
        'api/alimento/crear',
        views.CrearAlimento.as_view(),
    ),
    path(
        'api/alimento/listar',
        views.ListarAlimentos.as_view(),
    ),
    path(
        'api/alimento/actualizar/<pk>/',
        views.ActualizarAlimento.as_view(),
    ),
    path(
        'api/alimento/eliminar/<pk>/',
        views.EliminarAlimento.as_view(),
    ),
]
