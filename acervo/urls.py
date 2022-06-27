from django.urls import path
from .views import CategoriaObraCreate, AutorObraCreate, ObraCreate
from .views import CategoriaObraUpdate, AutorObraUpdate, ObraUpdate
from .views import CategoriaObraDelete, AutorObraDelete, ObraDelete
from .views import CategoriaObraList, AutorObraList, ObraList


urlpatterns = [

    #********************* Create ****************************
    path('categoria/create/', CategoriaObraCreate.as_view(), name='categoria-cadastro'),
    path('autor/create/', AutorObraCreate.as_view(), name='autor-cadastro'),
    path('obra/create/', ObraCreate.as_view(), name='obra-cadastro'),

    #********************* Update ****************************
    path('categoria/update/<uuid:pk>/', CategoriaObraUpdate.as_view(), name='categoria-update'),
    path('autor/update/<uuid:pk>/', AutorObraUpdate.as_view(), name='autor-update'),
    path('obra/update/<uuid:pk>/', ObraUpdate.as_view(), name='obra-update'),

    # ********************* Delete ****************************
    path('categoria/delete/<uuid:pk>/', CategoriaObraDelete.as_view(), name='categoria-delete'),
    path('autor/delete/<uuid:pk>/', AutorObraDelete.as_view(), name='autor-delete'),
    path('obra/delete/<uuid:pk>/', ObraDelete.as_view(), name='obra-delete'),

    # ********************* Lista ****************************
    path('categoria/list/', CategoriaObraList.as_view(), name='categoria-list'),
    path('autor/list/', AutorObraList.as_view(), name='autor-list'),
    path('obra/list/', ObraList.as_view(), name='obra-list'),

]