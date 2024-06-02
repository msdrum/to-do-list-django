from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
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

class Criar_tarefa(CreateView):
    model = Tarefa
    fields = '__all__'  # recebendo todos os campos do model para ser utilizado no form.
    success_url = reverse_lazy('tarefas') # O método reverse_lazy, redirecionará o usuário para a página indicada no parâmetro, após a criação do conteúdo no form.

class Editar_tarefa(UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')

