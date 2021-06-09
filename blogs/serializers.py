from rest_framework import serializers
from .models import Article,Comments

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model=Article
    fields=(
      'id',
      'title',
      'description',
      'body',
      'published'
    )


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comments
    fields=(
      'id',
      'comment'
      'published'
    )