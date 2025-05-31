from django_filters import rest_framework as filters
from .models import *

class DeveloperFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Developer
        fields = []

class PublisherFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',lookup_expr='icontains')

    class Meta:
        model = Publisher
        fields = []

class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',lookup_expr='icontains')

    class Meta:
        model = Category
        fields = []

class GameFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',lookup_expr='icontains')
    age_required = filters.NumberFilter(field_name='age_required',lookup_expr='gt')
    class Meta:
        model = Game
        fields = []