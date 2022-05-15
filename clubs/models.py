from django.db import models

# Create your models here.
class Clubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome=models.CharField(max_length=200)
    emblema=models.TextField(default=" ",null=True)
    cidade = models.TextField(default=" ",null=True)
    socios = models.TextField(default=" ",null=True)
    data_fundacao = models.TextField(default=" ",null=True)
    pais = models.TextField(default=" ",null=True)
    liga = models.TextField(default=" ",null=True)
    treinador = models.TextField(default=" ",null=True)
    valor = models.TextField(default=" ",null=True)
    estadio_nome = models.TextField(default=" ",null=True)
    estadio_lotacao = models.TextField(default=" ",null=True)
    colocacao = models.TextField(default=" ",null=True)
    def __str__(self):
        return (self.title)