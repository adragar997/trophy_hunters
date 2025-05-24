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

class PublisherGameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name','cover','trophy_count','price','release_date','age_required','category'
        ]

class DeveloperGameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Game
        fields = [
            'name', 'cover', 'trophy_count', 'price', 'release_date', 'age_required', 'category'
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
class CreateGameSerializer(serializers.ModelSerializer):
    appid = serializers.IntegerField(source='app_id')
    name = serializers.CharField()
    class Meta:
        model = Game
        fields = ['appid', 'name']

    def create(self, validated_data):
        app_id = validated_data.get('app_id')
        game = Game.objects.filter(app_id=app_id).first()
        if game:
            return game
        return Game.objects.create(**validated_data)

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