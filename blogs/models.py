from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
import uuid
# from user.models import User
from blog import settings
User=settings.AUTH_USER_MODEL

# Create your models here.
class Article(models.Model):
  title=models.CharField(max_length=70, blank=False, default='')
  description = models.CharField(max_length=200,blank=False, default='')
  body=models.TextField(blank=False)
  published = models.BooleanField(default=False)
  user=models.ForeignKey(User, related_name='article',on_delete=models.CASCADE,null=True)

  def __str__(self):
    return str(self.title)

  class Meta:
    ordering=['-published']

class Comments(models.Model):
  comment=models.TextField(null=True)
  user=models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True)
  published = models.DateTimeField(auto_now_add=True)
  article = models.ForeignKey(Article,related_name='article', on_delete=models.CASCADE, null=True)
  
  def __str__(self):
    return str(self.comment)
  
  class Meta:
    ordering=['-published']

