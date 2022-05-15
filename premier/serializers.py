from rest_framework import serializers
from .models import Premier

class PremierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Premier
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    