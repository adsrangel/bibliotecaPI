from django.views.generic import TemplateView


# biblioteca padrão
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Biblioteca customizada
from .models import CategoriaObra, AutorObra, Obra


# Create your views here.

#********************* Create ****************************

class CategoriaObraCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = CategoriaObra
    fields = ['name', 'description', 'delete_flag']
    template_name = 'acervo/categoria_obra.html'
    success_url = reverse_lazy('categoria-list')


class AutorObraCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = AutorObra
    fields = ['name', 'description', 'delete_flag']
    template_name = 'acervo/autor_obra.html'
    success_url = reverse_lazy('autor-list')

class ObraCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Obra
    fields = ['name', 'description', 'delete_flag', 'autor', 'categoria']
    template_name = 'acervo/obra.html'
    success_url = reverse_lazy('obra-list')

#********************* Updates ****************************

class CategoriaObraUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = CategoriaObra
    fields = ['name', 'description', 'delete_flag']
    template_name = 'acervo/categoria_obra.html'
    success_url = reverse_lazy('categoria-list')

class AutorObraUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = AutorObra
    fields = ['name', 'description', 'delete_flag']
    template_name = 'acervo/autor_obra.html'
    success_url = reverse_lazy('autor-list')

class ObraUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Obra
    fields = ['name', 'description', 'delete_flag', 'autor', 'categoria']
    template_name = 'acervo/obra.html'
    success_url = reverse_lazy('obra-list')

#********************* Delete ****************************

class CategoriaObraDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = CategoriaObra
    template_name = 'acervo/categoria_obra_delete.html'
    success_url = reverse_lazy('categoria-list')

class AutorObraDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = AutorObra
    template_name = 'acervo/autor_obra_delete.html'
    success_url = reverse_lazy('autor-list')

class ObraDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Obra
    template_name = 'acervo/obra_delete.html'
    success_url = reverse_lazy('obra-list')

#********************* List ****************************

class CategoriaObraList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = CategoriaObra
    template_name = 'acervo/categoria_obra_list.html'

class AutorObraList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = AutorObra
    template_name = 'acervo/autor_obra_list.html'

class ObraList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Obra
    template_name = 'acervo/obra_list.html'
