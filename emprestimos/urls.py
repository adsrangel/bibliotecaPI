from django.urls import path
from .views import EmprestimosCreate, EmprestimosUpdate, EmprestimosDelete, EmprestimosList

urlpatterns = [

    #********************* Create ****************************
    path('emprestimos/create/', EmprestimosCreate.as_view(), name='emprestimos-cadastro'),

    #********************* Update ****************************
    path('emprestimos/update/<uuid:pk>/', EmprestimosUpdate.as_view(), name='emprestimos-update'),

    # ********************* Delete ****************************
    path('emprestimos/delete/<uuid:pk>/', EmprestimosDelete.as_view(), name='emprestimos-delete'),

    # ********************* Lista ****************************
    path('emprestimos/list/', EmprestimosList.as_view(), name='emprestimos-list'),

]