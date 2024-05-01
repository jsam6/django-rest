from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

def index(request):
    players = Player.objects.all()
    print(players)
    return HttpResponse(players)
