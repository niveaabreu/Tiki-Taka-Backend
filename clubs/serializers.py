from rest_framework import serializers
from .models import Clubs

class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clubs
        fields=['id','nome','emblema','cidade','socios','data_fundacao','pais','liga',
        'treinador','valor','estadio_nome','estadio_lotacao','colocacao']
    