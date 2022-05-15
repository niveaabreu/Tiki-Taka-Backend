from django.shortcuts import render

# Create your views here.
from best_players import serializers
from .models import Clubs
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import ClubsSerializer
from requests import Request

@api_view(['GET'])
def clubs(request):
    try:
        teams=Clubs.objects.all()
    except:
        raise Http404
    finally:
        teams=Clubs.objects.all()
    serialized_note= ClubsSerializer(teams,many=True)
    print(serialized_note.data)
    return Response(serialized_note.data)

@api_view(['GET'])
def club(request,id):
    try:
        team,created=Clubs.objects.get_or_create(id = id)
        if created:
            request_profile=Request().get_club_profile(id)
            request_header = Request().get_club_header(id)

            team.id = request_profile['mainFacts']['id']
            team.nome = request_profile['mainFacts']['fullName']
            team.cidade = request_profile['mainFacts']['city']
            team.socios = request_profile['mainFacts']['members']
            team.pais = request_profile['mainFacts']['countryImage']
            team.data_fundacao = request_profile['mainFacts']['founding']

            team.estadio_nome = request_profile['stadium']['name']
            team.estadio_lotacao = request_profile['stadium']['totalCapacity']
            team.estadio_foto = request_profile['stadium']['image']

            team.liga = request_header['club']['leagueName']
            team.emblema = request_header['club']['image']
            team.colocacao = request_header['club']['rank']
            team.treinador = request_header['club']['coachName']
            team.valor = request_header['club']['marketValue']

            team.save()
    except:
        raise Http404

    finally:
        serialized_note= ClubsSerializer(team)
        return Response(serialized_note.data)