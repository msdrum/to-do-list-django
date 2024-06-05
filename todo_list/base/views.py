from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout  # Importa o logout, para que a função possa receber esse tipo de request

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from . models import Tarefa
# Create your views here.

class Pagina_login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tarefas')
        
    
    
class Pagina_registro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):  # Função para validar o registro du usuário e direcioná-lo para a página de tarefas (pelo reverse_lazy() acima).
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(Pagina_registro, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Pagina_registro, self).get(*args, **kwargs)
        
    

       
class Pagina_logout(LogoutView):
    template_name = 'base/logout.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('login') # Usar o reverse_lazy para redirecionar o usuário direto para a página de login, mesmo sem ter um template de logout.html



class Lista_tarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'tarefas'  # Mudando o nome dado pelo django de "object_list" para "tarefas".
    template_name = 'base/lista_tarefas.html' # Comando para mudar o sufixo criado pelo django do template. Por padrão o django cria "nome_que_vc_deu_list.html"

    def get_context_data(self, **kwargs):  # Esta função restringe o acesso à lista de tarefas pela lista do usuário logado, impedindo que ele acesse a lista de um outro usuário.
        context = super().get_context_data(**kwargs)
        context['tarefas'] = context['tarefas'].filter(usuario=self.request.user) # atenção no argumento de filter! usuario é o campo do models.py e user é comando do django!
        # context['tarefas'] = context['tarefas'].filter(completo=False).count()

        search_input = self.request.GET.get('search-area') or '' # search-area é o nome colocado no html, como se fosse um "getById() no JS".
        if search_input:
            context['tarefas'] = context['tarefas'].filter(titulo__icontains=search_input)
        
        context['search_input'] = search_input
        return context


class Detalhe_tarefa(LoginRequiredMixin, DetailView):
    model = Tarefa
    context_object_name = 'tarefa' # Mudando o nome do endpoint para "tarefa"
    template_name = 'base/detalhe_tarefa.html' # Comando para mudar o sufixo criado pelo django do template. Por padrão o django cria "nome_que_vc_deu_detail.html"


class Criar_tarefa(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'completo']  # recebendo todos os campos do model para ser utilizado no form.
    success_url = reverse_lazy('tarefas') # O método reverse_lazy, redirecionará o usuário para a página indicada no parâmetro, após a criação do conteúdo no form.

    def form_valid(self, form): # Função criada para as tarefas que forem criadas serem associadas ao usuário logado!
        form.instance.usuario = self.request.user  # Atenção no form.instance...o valor que deve ser passado é o campo usuario do models-->> form.instance.usuario
        return super(Criar_tarefa, self).form_valid(form)


class Editar_tarefa(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'completo'] 
    success_url = reverse_lazy('tarefas')


class Deletar_tarefa(LoginRequiredMixin, DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    success_url = reverse_lazy('tarefas')

