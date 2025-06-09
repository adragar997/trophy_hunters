import urllib.parse
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import serializers
from datetime import datetime
from .models import *

# Retrieve serialized data
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['name']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CategoryGameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name', 'cover', 'trophy_count', 'price', 'release_date', 'categories'
        ]

class PublisherGameSerializer(serializers.ModelSerializer):
    publishers = PublisherSerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name','cover','trophy_count','price','release_date', 'publishers'
        ]

class DeveloperGameSerializer(serializers.ModelSerializer):
    developers = DeveloperSerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name', 'cover', 'trophy_count', 'price', 'release_date', 'developers'
        ]

class DlcGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DLC
        exclude = ['game']

class GameGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ['id','game']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ['id','game']

class GameTrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        exclude = ['id','game']


class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    developers = DeveloperSerializer(many=True)
    publishers = PublisherSerializer(many=True)
    images = GameGallerySerializer(many=True)
    movies = GameTrailerSerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'app_id','name', 'description','cover', 'trophy_count', 'is_free', 'price', 'release_date', 'categories',
            'developers', 'publishers', 'images', 'movies'
        ]

class NewSerializer(serializers.ModelSerializer):
    cover = serializers.URLField(source='game.cover')
    name = serializers.CharField(source='game.name')
    class Meta:
        model = New
        fields = ['cover','name','title','date','url']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        exclude = ['id','game']

class GameDetailSerializer(serializers.ModelSerializer):
    images = GameGallerySerializer(many=True)
    movies = GameTrailerSerializer(many=True)
    trophies = AchievementSerializer(many=True)
    class Meta:
        model = Game
        fields = ['app_id','name', 'cover', 'trophy_count', 'description','is_free', 'price', 'release_date', 'images', 'movies', 'trophies']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id','user']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','profile']


class UserTrophySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='trophy.name')
    blocked_icon = serializers.URLField(source='trophy.blocked_icon')
    unlocked_icon = serializers.URLField(source='trophy.unlocked_icon')
    description = serializers.URLField(source='trophy.description')
    achieved = serializers.BooleanField()

    class Meta:
        model = UserTrophy
        fields = ['name', 'achieved','blocked_icon','unlocked_icon','description']

class UserGameTrophySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    cover = serializers.URLField()
    trophy_count = serializers.IntegerField()
    trophies = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['name', 'cover', 'trophy_count', 'trophies']

    def get_trophies(self, game):
        user = self.context.get('user')
        if not user:
            return []

        user_trophies = UserTrophy.objects.filter(user=user, trophy__game=game)
        return UserTrophySerializer(user_trophies, many=True).data

class OwnedGameSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    game = serializers.SerializerMethodField()

    class Meta:
        model = GameOwnership
        fields = ['username', 'game']

    def get_game(self, obj):
        return UserGameTrophySerializer(obj.game, context={'user': obj.user}).data

class ShopSerializer(serializers.ModelSerializer):
    header_image = serializers.URLField(source='cover')
    trophy_count = serializers.IntegerField(source='trophy_count')
    final = serializers.FloatField(source='price')
    date = serializers.DateField(source='release_date')

    class Meta:
        model = Game

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    firstname = serializers.CharField(allow_blank=True, required=False)
    lastname = serializers.CharField(allow_blank=True, required=False)
    avatar = serializers.ImageField(allow_null=True, required=False)
    banner = serializers.ImageField(allow_null=True, required=False)
    bio = serializers.CharField(allow_blank=True, required=False)
    birthdate = serializers.DateField(allow_null=True, required=False)

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        firstname = validated_data.pop('firstname')
        lastname = validated_data.pop('lastname')
        birthdate = validated_data.pop('birthdate')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
        )

        return Profile.objects.create(user=user, birth_date=birthdate,**validated_data)

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'banner', 'bio', 'birth_date']

#CREATE
class CreateCategorySerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='name')
    class Meta:
        model = Category
        fields = ['description']

class CreateScreenshotSerializer(serializers.ModelSerializer):
    path_full = serializers.URLField(source='url')
    class Meta:
        model = Gallery
        fields = ['path_full']

class CreateMovieSerializer(serializers.ModelSerializer):
    mp4_max = serializers.URLField(source='url')

    class Meta:
        model = Trailer
        fields = ['mp4_max']

    def to_internal_value(self, data):
        mp4_max_url = data.get('mp4', {}).get('max')
        return {'url': mp4_max_url}

class CreateReleaseDataSerializer(serializers.Serializer):
    date = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def to_internal_value(self, data):
        raw_date = data.get("date", "")
        formats = [
            "%d %b, %Y",
            "%b %d, %Y",
            "%d %b. %Y",
            "%b %d. %Y",
        ]

        parsed_date = None
        for fmt in formats:
            try:
                parsed_date = datetime.strptime(raw_date, fmt).date()
                break
            except ValueError:
                continue

        return {'date': parsed_date}

class CreateAchievementCountSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        return data.get('total',0)

class CreateGameSerializer(serializers.ModelSerializer):
    steam_appid = serializers.IntegerField(source='app_id')
    header_image = serializers.URLField(source='cover')
    name = serializers.CharField()
    short_description = serializers.CharField(source='description', required=False)
    achievements = CreateAchievementCountSerializer(source='trophy_count', required=False)
    release_date = CreateReleaseDataSerializer(required=False)
    is_free = serializers.BooleanField(required=False)
    categories = CreateCategorySerializer(many=True, required=False)
    developers = serializers.ListField(child=serializers.CharField(), required=False)
    publishers = serializers.ListField(child=serializers.CharField(), required=False)
    screenshots = CreateScreenshotSerializer(many=True, required=False)
    movies = CreateMovieSerializer(many=True, required=False)

    class Meta:
        model = Game
        fields = [
            'steam_appid',
            'header_image',
            'name',
            'release_date',
            'achievements',
            'is_free',
            'short_description',
            'categories',
            'developers',
            'publishers',
            'screenshots',
            'movies'
        ]

    def create(self, validated_data):
        app_id = validated_data.pop('app_id')
        categories_data = validated_data.pop('categories',[])
        developers_data = validated_data.pop('developers',[])
        publishers_data = validated_data.pop('publishers',[])
        release_data = validated_data.pop('release_date',None)
        date = release_data.get('date') if release_data else None
        screenshots_data = validated_data.pop('screenshots',[])
        movies_data = validated_data.pop('movies',[])

        game, _ = Game.objects.update_or_create(app_id=app_id, defaults={
            **validated_data,
            'release_date': date,
        })

        for movie_data in movies_data:
            movie, _ = Trailer.objects.get_or_create(game=game, **movie_data)

        for screenshot_data in screenshots_data:
            screenshot, _ = Gallery.objects.get_or_create(url=screenshot_data['url'], game=game)

        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(name=category_data['name'].lower())
            game.categories.add(category)

        for developer_name in developers_data:
            developer, _ = Developer.objects.get_or_create(name=developer_name.lower())
            game.developers.add(developer)

        for publisher_name in publishers_data:
            publisher, _ = Publisher.objects.get_or_create(name=publisher_name.lower())
            game.publishers.add(publisher)

        return game

class CreateTrophySerializer(serializers.ModelSerializer):
    displayName = serializers.CharField(source='name', required=False)
    name = serializers.CharField(source='api_name', required=False)
    hidden = serializers.BooleanField(required=False)
    description = serializers.CharField(required=False)
    icon = serializers.URLField(source='unlocked_icon', required=False)
    icongray = serializers.URLField(source='blocked_icon', required=False)

    class Meta:
        model = Trophy
        fields = ['displayName','hidden','description','icon','icongray','name']

    def create(self, validated_data):
        name = validated_data.pop('name')
        app_id = self.context.get('app_id')

        game = Game.objects.get(app_id=app_id)
        if game:
            trophy,_  = Trophy.objects.update_or_create(game=game, name=name, defaults=validated_data)
            return trophy

class CreateNewSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=False)
    url = serializers.CharField(required=False)
    date = serializers.IntegerField(required=False)

    class Meta:
        model = New
        fields = ['title','url','date']

    def create(self, validated_data):
        title = validated_data.pop('title')
        url_data = validated_data.pop('url')
        app_id = self.context.get('app_id')
        timestamp = validated_data.pop('date')
        date = datetime.fromtimestamp(timestamp).date()
        url = urllib.parse.quote(url_data, safe=':/')

        try:
            game = Game.objects.get(app_id=app_id)
        except Exception:
            return None

        new, _ = New.objects.update_or_create(game=game, title=title, defaults={**validated_data,'date':date, 'url':url})
        return new

class CreateOwnedGameSerializer(serializers.ModelSerializer):
    appid = serializers.IntegerField()

    class Meta:
        model = GameOwnership
        fields = ['appid']

    def create(self, validated_data):
        user = self.context.get('user')
        app_id = validated_data.pop('appid')

        game, created = Game.objects.get_or_create(app_id=app_id)

        ownership = GameOwnership.objects.get_or_create(user=user, game=game)
        return ownership

class CreateUserTrophySerializer(serializers.ModelSerializer):
    apiname = serializers.CharField()
    achieved = serializers.IntegerField()

    class Meta:
        model = UserTrophy
        fields = ['apiname','achieved']

    def create(self, validated_data):
        apiname = validated_data.pop('apiname')
        user = self.context['user']
        game = self.context['game']

        try:
            trophy = Trophy.objects.get(api_name=apiname, game=game)
        except Trophy.DoesNotExist:
            return None

        user_trophy,_ = UserTrophy.objects.update_or_create(user=user, trophy=trophy, defaults=validated_data)
        return user_trophy

class CreateProfileSerializer(serializers.ModelSerializer):
    username  = serializers.CharField(source='user.username', read_only=True)
    firstname = serializers.CharField(source='user.first_name', read_only=True)
    lastname  = serializers.CharField(source='user.last_name', read_only=True)
    avatar    = serializers.ImageField()
    banner    = serializers.ImageField()
    bio       = serializers.CharField()
    birth_date = serializers.DateField(read_only=True)

    class Meta:
        model  = Profile
        fields = ['username', 'firstname', 'lastname', 'avatar',
                  'banner', 'bio', 'birth_date']