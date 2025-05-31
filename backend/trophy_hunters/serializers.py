from rest_framework import serializers
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
    category = CategorySerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name', 'cover', 'trophy_count', 'price', 'release_date', 'age_required', 'category'
        ]

class PublisherGameSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name','cover','trophy_count','price','release_date','age_required','publisher'
        ]

class DeveloperGameSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name', 'cover', 'trophy_count', 'price', 'release_date', 'age_required', 'developer'
        ]

class DlcGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DLC
        exclude = ['game']

class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    developer = DeveloperSerializer(many=True)
    publisher = PublisherSerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'app_id','name', 'cover', 'trophy_count', 'price', 'release_date', 'age_required', 'category',
            'developer', 'publisher'
        ]

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        exclude = ['game']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        exclude = ['id','game']

class GameGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ['id','game']

class GameTrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        exclude = ['id','game']

class GameDetailSerializer(serializers.ModelSerializer):
    dlcs = DlcGameSerializer(many=True)
    images = GameGallerySerializer(many=True)
    trailers = GameTrailerSerializer(many=True)
    class Meta:
        exclude = ['id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

class OwnedGameSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    class Meta:
        model = GameOwnership
        exclude = ['user','id']

class ShopSerializer(serializers.ModelSerializer):
    header_image = serializers.URLField(source='cover')
    trophy_count = serializers.IntegerField(source='trophy_count')
    final = serializers.FloatField(source='price')
    date = serializers.DateField(source='release_date')
    required_age = serializers.IntegerField(source='age_required')
    class Meta:
        model = Game

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    avatar = serializers.ImageField()
    banner = serializers.ImageField()
    bio = serializers.CharField()
    birthdate = serializers.DateField()

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        firstname = validated_data.pop('firstname')
        lastname = validated_data.pop('lastname')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
        )
        birthdate = validated_data.pop('birthdate')

        return Profile.objects.create(user=user, birth_date=birthdate,**validated_data)

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

class CreateAchievementSerializer(serializers.Serializer):
    total = serializers.IntegerField()

class CreateGameSerializer(serializers.ModelSerializer):
    steam_appid = serializers.IntegerField(source='app_id')
    header_image = serializers.URLField(source='cover')
    name = serializers.CharField()
    required_age = serializers.IntegerField(source='age_required', required=False)
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
            'required_age',
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
        screenshots_data = validated_data.pop('screenshots',[])
        movies_data = validated_data.pop('movies',[])

        game, _ = Game.objects.get_or_create(app_id=app_id, **validated_data)

        for movie_data in movies_data:
            movie, _ = Trailer.objects.get_or_create(game=game, **movie_data)

        for screenshot_data in screenshots_data:
            screenshot, _ = Gallery.objects.get_or_create(url=screenshot_data['url'], game=game)

        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(name=category_data['name'])
            game.category.add(category)

        for developer_name in developers_data:
            developer, _ = Developer.objects.get_or_create(name=developer_name)
            game.developer.add(developer)

        for publisher_name in publishers_data:
            publisher, _ = Publisher.objects.get_or_create(name=publisher_name)
            game.publisher.add(publisher)

        return game

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