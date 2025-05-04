from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    appid = serializers.IntegerField(source='app_id')
    name = serializers.CharField()

    class Meta:
        model = Game
        fields = ['appid','name']

class ShopSerializer(serializers.ModelSerializer):
    header_image = serializers.URLField(source='cover')
    trophy_count = serializers.IntegerField(source='trophy_count')
    final = serializers.FloatField(source='price')
    date = serializers.DateField(source='release_date')
    required_age = serializers.IntegerField(source='age_required')
    class Meta:
        model = Game

class ProfileSerializer(serializers.Serializer):
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

        user = User.objects.create(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
        )
        birthdate = validated_data.pop('birthdate')

        return Profile.objects.create(user=user, birth_date=birthdate,**validated_data)