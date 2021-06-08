from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from .views import ArticleViewSet
from .models import Article
from .serializers import ArticleSerializer

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

app_name = 'articles'

urlpatterns = [
  path('', include(router.urls))
  # path('articles/', ArticleViewSet.as_view(queryset=Article.objects.select_related('author', 'author__user'),serializer_class=ArticleSerializer)),

]
