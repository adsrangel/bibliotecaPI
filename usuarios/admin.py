from django.contrib import admin
from .models import Periodo, TipoUsuario, Usuarios

# Register your models here.
admin.site.register(Periodo)
admin.site.register(TipoUsuario)
admin.site.register(Usuarios)
