from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.list_feedback, name='list_feedback'),
    path('create/<int:pk>/', views.criar_feedback, name='criar_feedback'),
    path('update/<int:pk>/', views.update_feedback, name='update_feedback'),
    path('delete/<int:pk>/', views.delete_feedback, name='delete_feedback'),
]
