from django.urls import path
from .views import PeriodoCreate, PeriodoUpdate, PeriodoDelete, PeriodoList
from .views import TipoUsuarioCreate, TipoUsuarioUpdate, TipoUsuarioDelete, TipoUsuarioList
from .views import UsuariosCreate, UsuariosUpdate, UsuariosDelete, UsuariosList

urlpatterns = [

    #********************* Create ****************************
    path('periodo/create/', PeriodoCreate.as_view(), name='periodo-cadastro'),
    path('tipo_usuario/create/', TipoUsuarioCreate.as_view(), name='tipo_usuario-cadastro'),
    path('usuarios/create/', UsuariosCreate.as_view(), name='usuarios-cadastro'),

    #********************* Update ****************************
    path('periodo/update/<uuid:pk>/', PeriodoUpdate.as_view(), name='periodo-update'),
    path('tipo_usuario/update/<uuid:pk>/', TipoUsuarioUpdate.as_view(), name='tipo_usuario-update'),
    path('usuarios/update/<uuid:pk>/', UsuariosUpdate.as_view(), name='usuarios-update'),

    # ********************* Delete ****************************
    path('periodo/delete/<uuid:pk>/', PeriodoDelete.as_view(), name='periodo-delete'),
    path('tipo_usuario/delete/<uuid:pk>/', TipoUsuarioDelete.as_view(), name='tipo_usuario-delete'),
    path('usuarios/delete/<uuid:pk>/', UsuariosDelete.as_view(), name='usuarios-delete'),

    # ********************* Lista ****************************
    path('periodo/list/', PeriodoList.as_view(), name='periodo-list'),
    path('tipo_usuario/list/', TipoUsuarioList.as_view(), name='tipo_usuario-list'),
    path('usuarios/list/', UsuariosList.as_view(), name='usuarios-list'),

]