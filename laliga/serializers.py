from rest_framework import serializers
from .models import Laliga

class LaligaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Laliga
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    