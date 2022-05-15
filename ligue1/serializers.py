from rest_framework import serializers
from .models import Ligue1

class Ligue1Serializer(serializers.ModelSerializer):
    class Meta:
        model=Ligue1
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    