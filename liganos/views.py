from django.shortcuts import render
# Create your views here.
from best_players import serializers
from .models import Liganos
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import LiganosSerializer
from requests import Request

@api_view(['GET'])
def liganos(request):
    try:
        teams=Liganos.objects.all()
        if teams.count()==0:
            request=Request().get_league_table('PO1')
            for teams in request['table']:
                table=Liganos(posicao=teams['rank'],foto=teams['clubImage'],nome=teams['clubName'],
                pontos=teams['points'],jogos=teams['matches'],vitorias=teams['wins'],empates=teams['draw'],
                derrotas=teams['losses'],saldo=teams['goalDifference'])
                table.save()
    except:
        raise Http404
    finally:
        teams=Liganos.objects.all()
    serialized_note= LiganosSerializer(teams,many=True)
    print(serialized_note.data)
    return Response(serialized_note.data)

