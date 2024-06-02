from django.urls import path
from . views import Lista_tarefas, Detalhe_tarefa, Criar_tarefa, Editar_tarefa


urlpatterns = [
    path('', 
         Lista_tarefas.as_view(),
         name='tarefas'
    ),

    path(
        'tarefa/<int:pk>/',
        Detalhe_tarefa.as_view(),
        name='tarefa'
    ),

     path('criar-tarefa', 
         Criar_tarefa.as_view(),
         name='criar-tarefa'
    ),

     path(
        'editar-tarefa/<int:pk>/',
        Editar_tarefa.as_view(),
        name='editar-tarefa'
    ),
]
