from rest_framework import serializers
from .models import Seriea

class SerieaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seriea
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    