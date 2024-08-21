from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.list_equipe, name='list_equipe'),
    path('create_equipe/', views.create_equipe, name='create_equipe'),
    path('update_equipe/<int:pk>/', views.update_equipe, name='update_equipe'),
    path('delete_equipe/<int:pk>/', views.delete_equipe, name='delete_equipe'),
]