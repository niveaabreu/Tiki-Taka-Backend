from django.db import models

# Create your models here.
class Players(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome=models.CharField(max_length=200)
    data=models.TextField(default=" ",null=True)
    pais = models.TextField(default=" ",null=True)
    idade = models.TextField(default=" ",null=True)
    altura = models.TextField(default=" ",null=True)
    clube = models.TextField(default=" ",null=True)
    valor = models.TextField(default=" ",null=True)
    numerodacamisa = models.TextField(default=" ",null=True)
    jogos = models.TextField(default=" ",null=True)
    gols = models.TextField(default=" ",null=True)
    assistencia = models.TextField(default=" ",null=True)
    image = models.TextField(default=" ",null=True)
    def __str__(self):
        return (self.title)