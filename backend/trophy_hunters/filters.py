from django_filters import rest_framework as filters
from .models import *

class DeveloperFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    start_with = filters.CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Developer
        fields = []

class PublisherFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',lookup_expr='icontains')
    start_with = filters.CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Publisher
        fields = []

class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',lookup_expr='icontains')
    start_with = filters.CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Category
        fields = []

class GameFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',lookup_expr='icontains')
    age_required = filters.NumberFilter(field_name='age_required',lookup_expr='gt')
    release_gt = filters.DateFilter(field_name='release_date',lookup_expr='gte')
    release_lt = filters.DateFilter(field_name='release_date',lookup_expr='lte')
    trophy_count = filters.NumberFilter(field_name='trophy_count',lookup_expr='gte')
    is_free = filters.BooleanFilter(field_name='is_free',lookup_expr='exact')

    class Meta:
        model = Game
        fields = []