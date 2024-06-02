from django.urls import path
from . views import Lista_tarefas, Detalhe_tarefa


urlpatterns = [
    path('', 
         Lista_tarefas.as_view(),
         name='tarefas'
    ),

    path(
        'tarefa/<int:pk>/',
        Detalhe_tarefa.as_view(),
        name='tarefa'
    )
]
