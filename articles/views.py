from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer


# Create your views here.
class ArticleViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):

  queryset = Article.objects.select_related('author', 'author__user')
  permission_classes = (IsAuthenticatedOrReadOnly,)
  serializer_class = ArticleSerializer

  def post(self, request):
    serializer_context = {'author': request.user.profile}
    serializer_data = request.data

    serializer = self.serializer_class(
      data=serializer_data, context=serializer_context
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def get(self,request, *args, **kwargs):
    serializer=self.serializer_class(Article.objects.all(),many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)