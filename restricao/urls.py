from django.urls import path
from . import views

urlpatterns = [
    path('criar_solicitacao/', views.criar_solicitacao, name='criar_solicitacao'),
    path('minhas_solicitacoes/', views.minhas_solicitacoes, name='minhas_solicitacoes'),
    path('listar_solicitacoes/', views.listar_solicitacoes, name='listar_solicitacoes'),
    path('delete_restricao/<int:id>/', views.delete_restricao, name='delete_restricao'),
    path('editar_restricao/<int:id>/', views.editar_restricao, name='editar_restricao'),
  
]