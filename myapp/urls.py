from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos, name='todos'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('edit/<id>', views.edit, name='edit')
]
