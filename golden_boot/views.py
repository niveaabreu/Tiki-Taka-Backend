from django.shortcuts import render

# Create your views here.
from best_players import serializers
from .models import Golden_Boot
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import Golden_bootSerializer
from requests import Request

@api_view(['GET'])
def golden(request):
    try:
        players=Golden_Boot.objects.all()
        if players.count()==0:
            request=Request().get_golden_boot()
            print(request)
            for player in request['player']:
                best=Golden_Boot(first_name=player['firstName'],surname=player['lastName'],club=player['clubImage'],
                matches=player['matches'],image=player['playerImage'],country=player['countryImage'],goals=player['goals'])
                best.save()
    except:
        raise Http404
    finally:
        players=Golden_Boot.objects.all()
    serialized_note= Golden_bootSerializer(players,many=True)
    print(serialized_note.data)
    return Response(serialized_note.data)