from django.urls import path

from .views import ArticleListview

app_instance = "blog"

urlpatterns = [
    path('api/articles/', ArticleListview.as_view(), name='article-list'),

]
