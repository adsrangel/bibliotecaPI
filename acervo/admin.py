from django.contrib import admin
from .models import AutorObra, CategoriaObra, Obra

# Register your models here.
admin.site.register(AutorObra)
admin.site.register(CategoriaObra)
admin.site.register(Obra)