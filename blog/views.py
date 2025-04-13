from rest_framework.generics import ListAPIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleListview(ListAPIView):
    queryset = Article.objects.all().order_by('-publication_date') 
    serializer_class = ArticleSerializer
