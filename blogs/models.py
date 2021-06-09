from django.db import models

# Create your models here.
class Article(models.Model):
  title=models.CharField(max_length=70, blank=False, default='')
  description = models.CharField(max_length=200,blank=False, default='')
  body=models.TextField(blank=False)
  published = models.BooleanField(default=False)

  
