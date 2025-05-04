from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import  views

urlpatterns = [
    # GET URLS
    path('games/', views.GetGames.as_view(), name='GetGames'),
    path('gameNews/<int:appid>/', views.GetGameNews.as_view(), name='GetGameNews'),
    path('player/<int:steamid>/', views.GetPlayerDetails.as_view(), name='GetPlayer'),
    path('player/<int:steamid>/games/', views.GetPlayerGames.as_view(), name='GetPlayerGames'),
    path('player/<int:steamid>/games/<int:appid>/', views.GetGameAchievements.as_view(), name='GetGameAchievements'),
    path('shop/<int:appid>/', views.GetShopDetails.as_view(), name='GetShopDetails'),
    path('steamid/<str:username>/', views.GetPlayerSteamid.as_view(), name='GetPlayerSteamid'),

    # FETCH URLS
    path('fetch-games/', views.FetchGamesData.as_view(), name='FetchGamesData'),
    path('fetch-shop/<int:appid>', views.FetchShopData.as_view(), name='FetchShopData'),

    # TOKENS
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh' ),

    # REGISTER
    path('register/', views.Register.as_view(), name='register'),
]