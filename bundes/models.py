from django.db import models

# Create your models here.
class Bundes(models.Model):
    posicao=models.CharField(max_length=200)
    foto=models.CharField(max_length=200)
    nome=models.TextField(default=" ",null=True)
    pontos=models.TextField(default=" ",null=True)
    jogos=models.TextField(default=" ",null=True)
    vitorias=models.TextField(default=" ",null=True)
    empates=models.TextField(default=" ",null=True)
    derrotas=models.TextField(default=" ",null=True)
    saldo=models.TextField(default=" ",null=True)
    def __str__(self):
        return (self.title)