from django.contrib import admin
from django.urls import path

# IMPORTAMOS LAS VISTAS GENERICAS
from . import views


urlpatterns = [
    path(
        'api/raza/crear',
        views.CrearRaza.as_view(),
    ),
    path(
        'api/animal/crear',
        views.CrearAnimal.as_view(),
    ),
    path(
        'api/animal/listar',
        views.ListarAnimales.as_view(),
    ),
    path(
        'api/animal/actualizar/<pk>',
        views.ActualizarAnimal.as_view(),
    ),
    path(
        'api/animal/eliminar/<pk>',
        views.EliminarAnimal.as_view(),
    ),
]
