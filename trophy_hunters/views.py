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
    def get(self, request, *args, **kwargs):
        url = f'{os.environ['URL_RESOLVE_VANITY']}'
        params = {
            'key' : f'{os.environ['STEAM_API_TOKEN']}',
            'vanityurl' : self.kwargs['username'],
        }
        data = requests.get(url, params=params).json()
        return Response(data=data, status=200)

class GetGameNews(APIView):
    def get(self, request, *args, **kwargs):
        url = f'{os.environ['URL_GAME_NEWS']}'
        params = {
            'key' : f'{os.environ['STEAM_API_TOKEN']}',
            'appid' : self.kwargs['appid'],
        }
        data = requests.get(url, params=params).json()
        return Response(data=data, status=200)

class GetGameAchievements(APIView):
    def get(self, request, *args, **kwargs):
        url = f'{os.environ['URL_PLAYER_GAME_ACHIEVEMENTS']}'
        url2 = f'{os.environ['URL_GAME_SCHEME']}'
        params = {
            'key' : f'{os.environ['STEAM_API_TOKEN']}',
            'appid' : self.kwargs['appid'],
            'steamid' : self.kwargs['steamid'],
        }
        data = requests.get(url2, params=params).json()
        return Response(data=data, status=200)

class GetPlayerDetails(APIView):
    def get(self, request, *args, **kwargs):
        url = f'{os.environ['URL_PLAYER_DETAILS']}'
        params = {
            'key' : f'{os.environ['STEAM_API_TOKEN']}',
            'steamids' : self.kwargs['steamid']
        }
        data = requests.get(url, params=params).json()
        return Response(data=data, status=200)

class GetPlayerGames(APIView):
    def get(self, request, *args, **kwargs):
        url = f'{os.environ['URL_PLAYER_GAMES']}'
        params = {
            'key' : f'{os.environ['STEAM_API_TOKEN']}',
            'steamid' : self.kwargs['steamid'],
        }
        data = requests.get(url, params=params).json()
        return Response(data=data, status=200)

class GetShopDetails(APIView):
    def get(self, request, *args, **kwargs):
        url = f'{os.environ['URL_SHOP_GAME']}'
        params = {
            'appids': self.kwargs['appid'],
        }
        data = requests.get(url, params=params).json()
        return Response(data=data, status=200)