from django.urls import path
from . views import Lista_de_tarefas


urlpatterns = [
    path('', 
         Lista_de_tarefas.as_view(),
         name='tarefas'
    ),
]
