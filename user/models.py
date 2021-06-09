from django.db import models
from blogs.models import Article

# Create your models here.
class Profile(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField()
  article=models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name

  def save_user(self):
    self.save()

  def delete_user(self):
    self.delete()

    