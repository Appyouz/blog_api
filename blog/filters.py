from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Article


class ArticleFilter(filters.FilterSet):
    publication_date = filters.DateFilter(field_name='publication_date', method='filter_by_publication_date')

    def filter_by_publication_date(self, queryset, name, value):
        return queryset.filter(publication_date__date=value)

    class Meta:
        model = Article
        fields = ['publication_date']
