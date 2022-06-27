import uuid
from django.db import models
from acervo.models import Obra
from usuarios.models import Usuarios

# Create your models here.

#********************************** Acervo ********************************************************



class Emprestimos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    delete_flag = models.BooleanField(null=True, blank=True, default=False, editable=True, verbose_name='Inativo?')
    observation = models.CharField(max_length=500, verbose_name='Descrição', null=True, blank=True)
    obra = models.ForeignKey(Obra, on_delete=models.PROTECT, verbose_name='Item do acervo')
    usuario = models.ForeignKey(Usuarios, on_delete=models.PROTECT, verbose_name='Usuario', null=True)
    data_emprestimo = models.DateField(null=True, blank=True)
    data_retorno = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Chave: {} ".format(self.id)

