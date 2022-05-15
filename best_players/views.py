from django.shortcuts import render

# Create your views here.
from best_players import serializers
from .models import Best_Player
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import Best_playerSerializer
from requests import Request

@api_view(['GET'])
def best(request):
    try:
        players=Best_Player.objects.all()
        if players.count()==0:
            request=Request().get_best_players()
            print(request)
            for player in request['player']:
                best=Best_Player(year=player['year'],first_name=player['firstName'],surname=player['lastName'],
                club=player['clubName'],value=player['clubImage'],image=player['playerImage'],country=player['countryImage'])
                best.save()
    except:
        raise Http404
    finally:
        players=Best_Player.objects.all()
    serialized_note=Best_playerSerializer(players,many=True)
    print(serialized_note.data)
    return Response(serialized_note.data)