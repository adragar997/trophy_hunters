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