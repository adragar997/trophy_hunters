from django.urls import path
from . import  views

urlpatterns = [
    path('games/', views.GameList.as_view(), name='GameList'),
]