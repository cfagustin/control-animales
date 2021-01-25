from django.contrib import admin
# IMPORTAR EL MODELO Alimento
from .models import Alimento, Tipo

# REGISTRAR EL MODELO Alimento Y Tipo
admin.site.register(Alimento)
admin.site.register(Tipo)