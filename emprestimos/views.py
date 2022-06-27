# biblioteca padrão
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Biblioteca customizada
from .models import Emprestimos


# Create your views here.

#********************* Create ****************************

class EmprestimosCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Emprestimos
    fields = ['obra', 'usuario', 'data_emprestimo', 'data_retorno', 'observation', 'delete_flag']
    template_name = 'emprestimos/emprestimos.html'
    success_url = reverse_lazy('emprestimos-list')


#********************* Updates ****************************

class EmprestimosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Emprestimos
    fields = ['obra', 'observation', 'delete_flag']
    template_name = 'emprestimos/emprestimos.html'
    success_url = reverse_lazy('emprestimos-list')


#********************* Delete ****************************

class EmprestimosDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Emprestimos
    template_name = 'emprestimos/emprestimos_delete.html'
    success_url = reverse_lazy('emprestimos-list')


#********************* List ****************************

class EmprestimosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Emprestimos
    template_name = 'emprestimos/emprestimos_list.html'

