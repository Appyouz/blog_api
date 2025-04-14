from django_filters import rest_framework as filters

from .models import Article, Tag


class ArticleFilter(filters.FilterSet):
    publication_date = filters.DateFilter(field_name='publication_date', method='filter_by_publication_date')
    tags = filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), field_name='tags')

    def filter_by_publication_date(self, queryset, name, value):
        return queryset.filter(publication_date__date=value)

    class Meta:
        model = Article
        fields = ['publication_date', 'tags']
