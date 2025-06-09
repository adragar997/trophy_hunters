import time
from celery_once import QueueOnce
import requests
from celery import shared_task
import os
from .models import Profile, Game
from .serializers import CreateOwnedGameSerializer, CreateTrophySerializer, CreateGameSerializer, CreateNewSerializer, \
    CreateUserTrophySerializer


@shared_task(queue="fast")
def user_games():
    try:
        profile = Profile.objects.filter(steam_processed=False).first()

        if not profile:
            print("no hay perfiles por procesar")
            return

        user = profile.user
        time.sleep(2)
        vanityurl = requests.get(f'{os.getenv('URL_USER_STEAMID')}', params={'key': f'{os.getenv('STEAM_API_KEY')}',
                                                                             'vanityurl': user.username}).json()
        if vanityurl['response']['success'] == 1:
            steam_id = vanityurl['response']['steamid']
            print(steam_id)
            profile.steam_id = steam_id
            profile.save()
            time.sleep(2)
            games = requests.get(f'{os.getenv('URL_USER_GAMES')}',
                                 params={'steamid': steam_id, 'key': f'{os.getenv('STEAM_API_KEY')}'}).json()
            serializer = CreateOwnedGameSerializer(data=games['response']['games'], many=True, context={
                'user': user,
            })
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
    except Exception as e:
        print(str(e))

@shared_task(queue="slow")
def games():
    try:
        games = Game.objects.all()
        #data = requests.get(f'{os.getenv('URL_GAME_LIST')}', {}).json()
        if not games:
            print("no hay juegos que procesar")
            return

        for game in games:
            app_id = str(game.app_id)
            details = requests.get(f'{os.getenv('URL_GAME_DETAILS')}', {'appids': app_id}).json()
            if details is not None and details[app_id]['success'] and details[app_id]['data']['type'] == 'game':
                print(app_id)
                serializer = CreateGameSerializer(data=details[app_id]['data'])
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                trophies = requests.get(f'{os.getenv('URL_TROPHY_LIST')}',
                                        {'appid': app_id, 'key': f'{os.getenv('STEAM_API_KEY')}'}).json()
                serializer = CreateTrophySerializer(
                    data=trophies['game'].get('availableGameStats', {}).get('achievements', []), many=True, context={
                        'app_id': app_id,
                    })
                if serializer.is_valid():
                   serializer.save()
                else:
                    print(serializer.errors)
                news = requests.get(f'{os.getenv('URL_GAME_NEWS')}', {'appid': app_id}).json()
                serializer = CreateNewSerializer(data=news['appnews']['newsitems'], many=True, context={
                    'app_id': app_id,
                })
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
    except Exception as e:
        print(str(e))

@shared_task(queue="fast")
def reset_users():
    try:
        profiles = Profile.objects.count()
        profiles_processed = Profile.objects.filter(steam_processed=True).count()

        if profiles == profiles_processed:
            Profile.objects.update(steam_processed=False)
            print("Perfiles reseteados")
    except Exception as e:
        print(str(e))

@shared_task(queue="fast")
def user_game_achievements():
    try:
        profile = Profile.objects.filter(steam_processed=False).first()

        if not profile:
            print("no hay perfiles por procesar")
            return

        user = profile.user
        games = Game.objects.filter(owners__user=user)
        if profile.steam_id:
            for game in games:
                time.sleep(2)
                user_trophies = requests.get(f'{os.getenv('URL_USER_GAME_TROPHIES')}', {
                    'key': f'{os.getenv('STEAM_API_KEY')}',
                    'appid': game.app_id,
                    'steamid': profile.steam_id
                }).json()
                if user_trophies['playerstats']['success'] and user_trophies['playerstats'].get('achievements'):
                    print(game.app_id)
                    serializer = CreateUserTrophySerializer(data=user_trophies['playerstats']['achievements'] , many=True, context={
                        'user': user,
                        'game':game,
                    })
                    if serializer.is_valid():
                        serializer.save()
                        print("trophy user saved")
                    else:
                        print(serializer.errors)
            profile.steam_processed = True
            profile.save(update_fields=['steam_processed'])
        return print("user has not vanity url active")
    except Exception as e:
        print(str(e))

