from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefa(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # A propriedade CASCADE vai fazer com que task seja apagada, quando o usuário for apagado.
        null=True,
        blank=True,
    )

    titulo = models.CharField(
        max_length=200,       
    )

    descricao= models.TextField(
        null=True,
        blank=True,
    )

    completo = models.BooleanField(
        default=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['completo'] 
