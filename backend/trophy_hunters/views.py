from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView
from adrf.views import APIView as AsyncAPIView
from .fetch_data import AsyncFetchData
from .serializers import *
from .filters import *
from asgiref.sync import sync_to_async
from rest_framework.permissions import IsAuthenticated
import os
from .models import *

class GetGames(ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    filterset_class = GameFilter
    serializer_class = GameSerializer

# terminar de arreglarlo
class GetGameDetails(ListAPIView):
    serializer_class = GameDetailSerializer()

    def get_queryset(self):
        queryset = Game.objects.prefetch_related('category', 'developer', 'gallery', 'trailer', 'publisher', 'dlc')
        app_id = self.kwargs.get('app_id')
        return queryset.filter(app_id=app_id)

class GetGameDlcs(ListAPIView):
    serializer_class = DlcGameSerializer

    def get_queryset(self):
        app_id = self.kwargs.get('app_id')
        return DLC.objects.filter(game__app_id=app_id)

class GetGameImages(ListAPIView):
    serializer_class = GameGallerySerializer

    def get_queryset(self):
        app_id = self.kwargs.get('app_id')
        return Gallery.objects.filter(game__app_id=app_id)

class GetGameTrailers(ListAPIView):
    serializer_class = GameTrailerSerializer

    def get_queryset(self):
        app_id = self.kwargs.get('app_id')
        return Trailer.objects.filter(game__app_id=app_id)

class GetGameNews(ListAPIView):
    serializer_class = NewSerializer

    def get_queryset(self):
        app_id = self.kwargs['appid']
        return New.objects.filter(game=app_id)

class GetNews(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    pagination_class = PageNumberPagination
    page_size = 20

class GetPublishers(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filterset_class = PublisherFilter
    pagination_class = PageNumberPagination
    page_size = 20

class GetPublisherGames(ListAPIView):
    serializer_class = PublisherGameSerializer
    pagination_class = PageNumberPagination
    page_size = 20

    def get_queryset(self):
        publisher_name = self.kwargs['publisher_name']
        return Game.objects.filter(publisher__name=publisher_name)

class GetDevelopers(ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    filterset_class = DeveloperFilter
    pagination_class = PageNumberPagination
    page_size = 20

class GetDeveloperGames(ListAPIView):
    serializer_class = DeveloperGameSerializer
    pagination_class = PageNumberPagination
    page_size = 20

    def get_queryset(self):
        developer_name = self.kwargs['developer_name']
        return Game.objects.filter(developer__name=developer_name)

class GetCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    pagination_class = PageNumberPagination
    page_size = 20

class GetCategoryGames(ListAPIView):
    serializer_class = CategoryGameSerializer
    pagination_class = PageNumberPagination
    paginate_by = 20

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Game.objects.filter(category__name=category_name)

# add pagination?
class GetGameAchievements(ListAPIView): 
    serializer_class = AchievementSerializer

    def get_queryset(self):
        app_id = self.kwargs['appid']
        return Trophy.objects.filter(game=app_id)

class GetPlayerDetails(ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Profile.objects.filter(user__username = username)

class GetPlayerGames(ListAPIView):
    serializer_class = OwnedGameSerializer
    pagination_class = PageNumberPagination
    paginate_by = 20

    def get_queryset(self):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        return user.owned_games.all()
#
class FetchGamesData(AsyncAPIView):
    async def get(self, request, *args, **kwargs):
        try:
            fetch_data = AsyncFetchData()
            url = f'{os.getenv('URL_GAME_LIST')}'
            data = await fetch_data.create_session(url, {})
            for game in data['applist']['apps']:
                if game['name']:
                    app_id = str(game['appid'])
                    url_details = f'{os.getenv('URL_GAME_DETAILS')}'
                    details = await fetch_data.create_session(url_details, {'appids': app_id})
                    if details[app_id]['success'] and details[app_id]['data']['type'] == 'game':
                        serializer = CreateGameSerializer(data= details[app_id]['data'])
                        if serializer.is_valid():
                            await sync_to_async(serializer.save)()
                        else:
                            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class Register(AsyncAPIView):
    parser_classes = [MultiPartParser, FormParser]
    async def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            await sync_to_async(serializer.save)()
            return Response(data={'message':'success'}, status=200)
        return Response(serializer.errors, status=400)

"""class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = CreateProfileSerializer(profile, context={'request': request})
        return Response(data=serializer.data, status=200)"""