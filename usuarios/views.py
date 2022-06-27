# biblioteca padrão
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Biblioteca customizada
from .models import Periodo, TipoUsuario, Usuarios


# Create your views here.

#********************* Create ****************************

class PeriodoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Periodo
    fields = ['name', 'description', 'delete_flag']
    template_name = 'usuarios/periodo.html'
    success_url = reverse_lazy('periodo-list')

class TipoUsuarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = TipoUsuario
    fields = ['name', 'description', 'delete_flag']
    template_name = 'usuarios/tipo_usuario.html'
    success_url = reverse_lazy('tipo_usuario-list')

class UsuariosCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Usuarios
    fields = ['name', 'ra_gr', 'periodo', 'tipo_usuario', 'serie', 'tel', 'email', 'description', 'delete_flag']
    template_name = 'usuarios/usuarios.html'
    success_url = reverse_lazy('usuarios-list')


#********************* Updates ****************************

class PeriodoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Periodo
    fields = ['name', 'description', 'delete_flag']
    template_name = 'usuarios/periodo.html'
    success_url = reverse_lazy('periodo-list')

class TipoUsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = TipoUsuario
    fields = ['name', 'description', 'delete_flag']
    template_name = 'usuarios/tipo_usuario.html'
    success_url = reverse_lazy('tipo_usuario-list')

class UsuariosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Usuarios
    fields = ['name', 'ra_gr', 'periodo', 'tipo_usuario', 'serie', 'tel', 'email', 'description', 'delete_flag']
    template_name = 'usuarios/usuarios.html'
    success_url = reverse_lazy('usuarios-list')

#********************* Delete ****************************

class PeriodoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Periodo
    template_name = 'usuarios/periodo_delete.html'
    success_url = reverse_lazy('periodo-list')

class TipoUsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = TipoUsuario
    template_name = 'usuarios/tipo_usuario_delete.html'
    success_url = reverse_lazy('tipo_usuario-list')

class UsuariosDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Usuarios
    template_name = 'usuarios/usuarios_delete.html'
    success_url = reverse_lazy('usuarios-list')

#********************* List ****************************

class PeriodoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Periodo
    template_name = 'usuarios/periodo_list.html'

class TipoUsuarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = TipoUsuario
    template_name = 'usuarios/tipo_usuario_list.html'

class UsuariosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Usuarios
    template_name = 'usuarios/usuarios_list.html'