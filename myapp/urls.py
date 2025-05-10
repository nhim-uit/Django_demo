from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos, name='Todos'),
    path('todos/create', views.create, name='Create')
]
