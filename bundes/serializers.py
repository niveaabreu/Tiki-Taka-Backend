from rest_framework import serializers
from .models import Bundes

class BundesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bundes
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    