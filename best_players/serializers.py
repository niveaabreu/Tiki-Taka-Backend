from rest_framework import serializers
from .models import Best_Player

class Best_playerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Best_Player
        fields=['id','year','first_name','surname','club','value','image','country']
    