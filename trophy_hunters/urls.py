from django.urls import path
from . import  views

urlpatterns = [
    path('games/', views.GetGames.as_view(), name='GetGames'),
    path('gameNews/<int:appid>/', views.GetGameNews.as_view(), name='GetGameNews'),
    path('gameAchievements/<int:appid>/', views.GetGameAchievements.as_view(), name='GetGameAchievements'),
    path('player/<int:steamid>/', views.GetPlayerDetails.as_view(), name='GetPlayer'),
    path('player/<int:steamid>/games/', views.GetPlayerGames.as_view(), name='GetPlayerGames'),
    path('shop/<int:appid>/', views.GetShopDetails.as_view(), name='GetShopDetails'),
    path('steamid/<str:username>/', views.GetPlayerSteamid.as_view(), name='GetPlayerSteamid'),
]