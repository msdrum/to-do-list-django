from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import Tarefa
# Create your views here.

class Lista_tarefas(ListView):
    model = Tarefa

    context_object_name = 'tarefas'  # Mudando o nome dado pelo django de "object_list" para "tarefas"

    template_name = 'base/lista_tarefas.html' # Comando para mudar o sufixo criado pelo django do template. Por padrão o django cria "nome_que_vc_deu_list.html"


class Detalhe_tarefa(DetailView):

    model = Tarefa

    context_object_name = 'tarefa' # Mudando o nome do endpoint para "tarefa"

    template_name = 'base/detalhe_tarefa.html' # Comando para mudar o sufixo criado pelo django do template. Por padrão o django cria "nome_que_vc_deu_detail.html"