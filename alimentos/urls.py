from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.list_alimentos, name='list_alimentos'),
    path('create_alimento/', views.create_alimento, name='create_alimento'),
    path('update_alimento/<int:pk>/', views.update_alimento, name='update_alimento'),
    path('delete_alimento/<int:pk>/', views.delete_alimento, name='delete_alimento'),
]