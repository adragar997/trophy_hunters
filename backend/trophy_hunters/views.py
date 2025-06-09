from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from adrf.views import APIView as AsyncAPIView, APIView
from .serializers import *
from .filters import *
from asgiref.sync import sync_to_async
from rest_framework.permissions import IsAuthenticated
from .models import *

class GetGames(ListAPIView):
    queryset = Game.objects.all().order_by('-release_date')
    filterset_class = GameFilter
    serializer_class = GameSerializer

class GetGameDetails(RetrieveAPIView):
    serializer_class = GameDetailSerializer
    lookup_field = 'app_id'

    def get_queryset(self):
        return Game.objects.all()

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
    queryset = New.objects.all().order_by('-date')
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
        return Game.objects.filter(publishers__name__icontains=publisher_name)

class GetDevelopers(ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    filterset_class = DeveloperFilter
    pagination_class = PageNumberPagination
    page_size = 20

class GetDeveloperGames(ListAPIView):
    serializer_class = DeveloperGameSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        developer_name = self.kwargs['developer_name']
        return Game.objects.filter(developers__name__icontains=developer_name)

class GetCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    pagination_class = PageNumberPagination
    page_size = 20

class GetCategoryGames(ListAPIView):
    serializer_class = CategoryGameSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Game.objects.filter(categories__name__icontains=category_name)

class GetGameAchievements(ListAPIView):
    serializer_class = AchievementSerializer

    def get_queryset(self):
        app_id = self.kwargs['appid']
        return Trophy.objects.filter(game=app_id)

class GetPlayerDetails(ListAPIView):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Profile.objects.filter(user__username = username)

class GetPlayerGames(ListAPIView):
    serializer_class = OwnedGameSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        return GameOwnership.objects.filter(user=user).order_by('game__name')

class GetProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class RegisterProfile(AsyncAPIView):
    parser_classes = [MultiPartParser, FormParser]
    async def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                await sync_to_async(serializer.save)()
                return Response(data={'message': 'success'}, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class UpdateProfile(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    async def patch(self, request, *args, **kwargs):
        try:
            profile_instance, created = await sync_to_async(Profile.objects.get_or_create)(user=request.user)

            serializer = UpdateProfileSerializer(instance=profile_instance, data=request.data, partial=True)

            if await sync_to_async(serializer.is_valid)(raise_exception=True):
                await sync_to_async(serializer.save)()
                return Response(
                    {"message": "Perfil actualizado con éxito.", "profile": serializer.data},
                    status=200
                )

        except Exception as e:
            return Response(
                {"error": "Ocurrió un error en el servidor: " + str(e)},
                status=500
            )