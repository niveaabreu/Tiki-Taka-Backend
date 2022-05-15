from rest_framework import serializers
from .models import Brasileirao

class BrasileiraoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brasileirao
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    