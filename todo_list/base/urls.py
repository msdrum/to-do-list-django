from django.urls import path
from . views import Lista_tarefas, Detalhe_tarefa, Criar_tarefa, Editar_tarefa, Deletar_tarefa, Pagina_login, Pagina_logout, Pagina_registro


urlpatterns = [

    path('login/', Pagina_login.as_view(), name='login'), 
    path('logout/', Pagina_logout.as_view(), name='logout'),
    path('registro/', Pagina_registro.as_view(), name='registro'),

    path('', Lista_tarefas.as_view(), name='tarefas'),
    path('tarefa/<int:pk>/', Detalhe_tarefa.as_view(), name='tarefa'),
    path('criar-tarefa', Criar_tarefa.as_view(), name='criar-tarefa'),
    path('editar-tarefa/<int:pk>/', Editar_tarefa.as_view(), name='editar-tarefa'),
    path('deletar-tarefa/<int:pk>/', Deletar_tarefa.as_view(), name='deletar-tarefa'),
]
