from rest_framework import serializers
from .models import Golden_Boot

class Golden_bootSerializer(serializers.ModelSerializer):
    class Meta:
        model=Golden_Boot
        fields=['id','first_name','surname','club','matches','image','country','goals']
    