from django.shortcuts import render

# Create your views here.
from best_players import serializers
from .models import Players
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import PlayersSerializer
from requests import Request

@api_view(['GET'])
def players(request):
    try:
        players=Players.objects.all()
    except:
        raise Http404
    finally:
        players=Players.objects.all()
    serialized_note= PlayersSerializer(players,many=True)
    print(serialized_note.data)
    return Response(serialized_note.data)

@api_view(['GET'])
def player(request,id):
    try:
        player,created=Players.objects.get_or_create(id = id)
        if created:
            request_perfomance=Request().get_player_performace(id)
            request_profile = Request().get_player_profile(id)
            
            player.nome = request_profile['playerProfile']['playerName']
            player.data = request_profile['playerProfile']['dateOfBirth']
            player.pais = request_profile['playerProfile']['internationalTeamImage']
            player.idade = request_profile['playerProfile']['age']
            player.altura = request_profile['playerProfile']['height']
            player.clube = request_profile['playerProfile']['clubImage']
            player.valor = request_profile['playerProfile']['marketValue']
            player.numerodacamisa = request_profile['playerProfile']['playerShirtNumber']
            player.image = request_profile['playerProfile']['playerImage']

            jogos=0
            gols=0
            assistencias=0
            
            for stats in request_perfomance["competitionPerformanceSummery"]:
                gols += int(stats["performance"]["goals"])
                jogos += int(stats["performance"]["matches"])
                assistencias += int(stats["performance"]["assists"])
            player.jogos = jogos
            player.gols = gols
            player.assistencia = assistencias
            player.save()
    except:
        raise Http404

    finally:
        serialized_note= PlayersSerializer(player)
        return Response(serialized_note.data)