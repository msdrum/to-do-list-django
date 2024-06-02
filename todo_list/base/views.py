from django.shortcuts import render
from django.views.generic.list import ListView
from . models import Tarefa
# Create your views here.

class Lista_de_tarefas(ListView):
    model = Tarefa