from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleListview(ListCreateAPIView):
    queryset = Article.objects.all().order_by('-publication_date') 
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleDetailView(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

