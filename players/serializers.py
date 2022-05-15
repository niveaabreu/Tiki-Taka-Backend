from rest_framework import serializers
from .models import Players

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Players
        fields=['id','nome','data','pais','idade','altura','clube','valor',
        'numerodacamisa','jogos','gols','assistencia','image']
    