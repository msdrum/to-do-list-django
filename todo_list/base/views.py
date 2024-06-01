from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def lista_de_tarefas(request):
    return HttpResponse("Opa!")