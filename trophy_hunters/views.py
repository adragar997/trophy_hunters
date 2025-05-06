from django.contrib.sites import requests
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from adrf.views import APIView as AsyncAPIView
from .fetch_data import AsyncFetchData
from .serializers import *
from asgiref.sync import sync_to_async
from rest_framework.permissions import IsAuthenticated
import requests
import os
from .models import *

class GetGames(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = PageNumberPagination

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

class GetPlayerDetails(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

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

class FetchGamesData(AsyncAPIView):
    async def get(self, request, *args, **kwargs):
        try:
            url = f'{os.getenv('URL_GAME_LIST')}'
            data = await AsyncFetchData().create_session(url)
            games = [game for game in data['applist']['apps'] if game['name']]

            for game in games:
                serializer = GameSerializer(data=game)
                if serializer.is_valid():
                    await sync_to_async(serializer.save)()
                else:
                    return Response(serializer.errors, status=400)
            return Response({'message': 'Games was successfully saved'}, status=200)
        except Exception as e:
            return Response({'error': e}, status=500)

class FetchShopData(AsyncAPIView):
    async def get(self, request, *args, **kwargs):
        try:
            url = f'{os.getenv('URL_SHOP_GAME')}'
            params = {
                'appids': self.kwargs['appid'],
            }
            data = await AsyncFetchData().create_session(url, params)

            for game_data in data[self.kwargs['appid']]['data']:
                serializer = ShopSerializer(data=game_data)
            return Response(data=data, status=200)
        except Exception as e:
            return Response({'error': e}, status=500)

class Register(AsyncAPIView):
    parser_classes = [MultiPartParser, FormParser]
    async def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            await sync_to_async(serializer.save)()
            return Response(data={'message':'success'}, status=200)
        return Response(serializer.errors, status=400)

class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(data=serializer.data, status=200)