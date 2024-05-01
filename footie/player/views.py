from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from common.util import response

def index(request):
    players = Player.objects.all()
    return response(list(players), 200)
