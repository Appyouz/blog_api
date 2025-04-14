from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .filters import ArticleFilter
from .models import Article
from .serializers import ArticleSerializer


class ArticleListview(ListCreateAPIView):
    queryset = Article.objects.all().order_by('-publication_date')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter

class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

