from rest_framework import serializers
from .models import Liganos

class LiganosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Liganos
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    