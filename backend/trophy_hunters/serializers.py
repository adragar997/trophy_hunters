from rest_framework import serializers
from .models import *

# Retrieve serialized data
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

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

class ProfileSerializer(serializers.ModelSerializer):
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