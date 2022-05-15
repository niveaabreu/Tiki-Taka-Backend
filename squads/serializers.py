from rest_framework import serializers
from .models import Squads

class SquadsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Squads
        fields=['id','club_id','name','image','age','shirtNumber']