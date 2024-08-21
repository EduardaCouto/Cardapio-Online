from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.cardapio_list, name='cardapio_list'),
    path('create/', views.cardapio_create, name='cardapio_create'),
    path('update/<int:pk>/', views.cardapio_update, name='cardapio_update'),
    path('delete/<int:pk>/', views.cardapio_delete, name='cardapio_delete'),
    path('delete_all/<int:pk>/', views.delete_all_cardapio, name='delete_all_cardapio'),
]
