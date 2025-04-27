from django.contrib.sites import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import requests
import os

class GetGames(APIView):
    def get(self, request):
        url = f'{os.environ['URL_GAME_LIST']}'
        games = []
        data = requests.get(url).json()

        for game in data['applist']['apps']:
            if game['name'] != "":
                games.append(game)

        return Response(data=games, status=200)

class GetPlayerSteamid(APIView):
    pass

class GetGameNews(APIView):
    pass

class GetGameAchievements(APIView):
    pass

class GetPlayerDetails(APIView):
    pass

class GetPlayerGames(APIView):
    pass

class GetShopDetails(APIView):
    pass