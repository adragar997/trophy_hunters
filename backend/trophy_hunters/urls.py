from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import  views

urlpatterns = [
    # GET URLS
    path('games/', views.GetGames.as_view(), name='GetGames'),
    path('games/<int:app_id>', views.GetGameDetails.as_view(), name='GetGameDetails'),
    path('dlcs/<int:app_id>/', views.GetGameDlcs.as_view(), name='GetGameDlcs'),
    path('images/<int:app_id>/', views.GetGameImages.as_view(), name='GetGameImages'),
    path('trailers/<int:app_id>/', views.GetGameTrailers.as_view(), name='GetGameTrailers'),
    path('news/', views.GetNews.as_view(), name='GetNews'),
    path('news/<int:appid>/', views.GetGameNews.as_view(), name='GetGameNews'),
    path('publishers/', views.GetPublishers.as_view(), name='GetPublishers'),
    path('publishers/<str:publisher_name>', views.GetPublisherGames.as_view(), name='GetPublisherGames'),
    path('developers/', views.GetDevelopers.as_view(), name='GetDevelopers'),
    path('developers/<str:developer_name>', views.GetDeveloperGames.as_view(), name='GetDeveloperGames'),
    path('categories/', views.GetCategories.as_view(), name='GetCategories'),
    path('categories/<str:category_name>', views.GetCategoryGames.as_view(), name='GetCategoryGames'),
    path('users/<str:username>', views.GetPlayerDetails.as_view(), name='GetPlayer'),
    path('users/<str:username>/games/', views.GetPlayerGames.as_view(), name='GetPlayerGames'),
    path('achievements/<int:appid>', views.GetGameAchievements.as_view(), name='GetGameAchievements'),

    # REGISTER
    path('register/', views.RegisterProfile.as_view(), name='RegisterProfile'),

    #UPDATE
    path('update/', views.UpdateProfile.as_view(), name='UpdateProfile'),

    #PROFILE
    path('profile/me/', views.GetProfile.as_view(), name='profile'),

    #TOKEN
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    #API DOCS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]