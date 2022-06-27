import uuid
from django.db import models

# Create your models here.

#********************************** Acervo ********************************************************

class Periodo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    delete_flag = models.BooleanField(null=True, blank=True, default=False, editable=True, verbose_name='Inativo?')
    description = models.CharField(max_length=500, verbose_name='Descrição', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return "{} ".format(self.name)

class TipoUsuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    delete_flag = models.BooleanField(null=True, blank=True, default=False, editable=True, verbose_name='Inativo?')
    description = models.CharField(max_length=500, verbose_name='Descrição', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return "{} ".format(self.name)

class Usuarios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    delete_flag = models.BooleanField(null=True, blank=True, default=False, editable=True, verbose_name='Inativo?')
    description = models.CharField(max_length=500, verbose_name='Descrição', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Nome')
    ra_gr = models.CharField(max_length=50, verbose_name='RA / RG', help_text='Informe o RA (para alunos) ou o RG (para professor)')
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    serie = models.CharField(max_length=50, verbose_name='Série')
    tel = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.CharField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return "{} ".format(self.name)