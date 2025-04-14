from django.urls import path

from .views import ArticleDetailView, ArticleListview

app_instance = "blog"

urlpatterns = [
    path('api/articles/', ArticleListview.as_view(), name='article-list'),
    path('api/articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),

]
