import uuid
from django.db import models

# Create your models here.

#********************************** Acervo ********************************************************

class AutorObra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    delete_flag = models.BooleanField(null=True, blank=True, default=False, editable=True, verbose_name='Inativo?')
    name = models.CharField(max_length=50, verbose_name='Nome')
    description = models.CharField(max_length=500, verbose_name='Descrição', null=True, blank=True)

    def __str__(self):
       return "{}".format(self.name)


class CategoriaObra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    delete_flag = models.BooleanField(null=True, blank=True, default=False, editable=True, verbose_name='Inativo?')
    name = models.CharField(max_length=50, verbose_name='Nome', editable=True)
    description = models.CharField(max_length=500, verbose_name='Descrição', editable=True, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Obra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    delete_flag = models.BooleanField(null=True, blank=True, default=False, editable=True, verbose_name='Inativo?')
    name = models.CharField(max_length=50, verbose_name='Nome')
    description = models.CharField(max_length=500, verbose_name='Descrição', null=True, blank=True)
    autor = models.ForeignKey(AutorObra, on_delete=models.PROTECT)
    categoria = models.ForeignKey(CategoriaObra, on_delete=models.PROTECT)

    def __str__(self):
        return "Obra: {} / Autor:'{}' / Categoria:'{}'".format(self.name, self.autor, self.categoria)

