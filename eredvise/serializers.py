from rest_framework import serializers
from .models import Eredvise

class EredviseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eredvise
        fields=['id','posicao','foto','nome','pontos','jogos','vitorias','empates',
        'derrotas','saldo']
    