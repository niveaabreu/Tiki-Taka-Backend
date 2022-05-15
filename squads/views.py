from django.shortcuts import render
# Create your views here.
from best_players import serializers
from .models import Squads
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import SquadsSerializer
from requests import Request

@api_view(['GET'])
def squads(request,id):
    try:
        squad = Squads.objects.filter(club_id=id)
        if squad.count() == 0:
            request_squad=Request().get_squad(id)
            print(request_squad['squad'][0])
            for player in request_squad['squad']:
                print('Entrei')
                player = Squads(id=player['id'],club_id=id, name = player['name'],image = player['image'],
                age = player['age'],shirtNumber = player['shirtNumber'])
                player.save()
            
    except:
        raise Http404
    finally:
        squad = Squads.objects.filter(club_id=id)
        serialized_note= SquadsSerializer(squad,many=True)
        return Response(serialized_note.data)