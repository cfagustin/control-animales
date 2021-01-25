from django.contrib import admin
# IMPORTAR EL MODELO Raza
from .models import Raza


# REGISTRAR EL MODELO Raza
admin.site.register(Raza)