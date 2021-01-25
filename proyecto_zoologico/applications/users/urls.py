
from django.contrib import admin
from django.urls import path

# IMPORTAMOS LAS VISTAS GENERICAS
from . import views


urlpatterns = [
    path(
        'api/usuario/crear',
        views.CrearUsuario.as_view(),
    ),

]
