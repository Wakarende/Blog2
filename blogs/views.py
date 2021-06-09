from django.shortcuts import render,HttpResponse,Http404

# Create your views here.
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JsonParser
from rest_framework import status


class ArticleView(APIView):
  serializer_class = ArticleSerializer
  model = Article

  def get_article(self, pk,format=None):
    try:
      return Articly.objects.get(pk=pk)
    except Article.DoesNotExist:
      raise Http404

  def get(self, request, format=None, *args, **kwargs):
    all_articles = Article.objects.all()
    serializers = self.serializer_class(all_articles, many=True)
    return Response(serializers.data)

  def post(self, request, format=None, *args, **kwargs):
    serializers = ArticleSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None,*args, **kwargs):
    pk = self.kwargs.get('pk')
    article = self.get_article(pk)
    serializers = ArticleSerializer(article, request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None, *args, **kwargs):
    article = self.get_article(pk)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  
class singleArticleView(APIView):
  serializer_class = ArticleSerializer
  def get_article(self, pk):
    try:
      return Article.objects.get(pk=pk)
    except Article.DoesNotExist:
      return Http404()

  def get(self, request, pk, format=None):
    post = self.get_article(pk)
    serializers = self.serializer_class(post)
    return Response(serializers.data)


