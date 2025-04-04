from django.contrib.sites import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import requests
import os

class GameList(APIView):
    def get(self, request):
        url = f'{os.environ['URL_GAME_LIST']}'
        games = []
        data = requests.get(url).json()

        for game in data['applist']['apps']:
            if game['name'] != "":
                games.append(game)

        return Response(data=games, status=200)