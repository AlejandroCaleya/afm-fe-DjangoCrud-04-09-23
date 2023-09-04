from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('delete/', views.delete, name='delete'),
    path('updatear/', views.updatear, name='updatear'),
    path('create/', views.create, name='create'),
]