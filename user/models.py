from django.db import models
from blogs.models import Article
from django.contrib.auth.models import AbstractUser
import  uuid
from django.contrib.auth.models import User
# Create your models here.
# class Profile(models.Model):
#   name=models.CharField(max_length=50)
#   email=models.EmailField()
#   article=models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

#   def __str__(self):
#     return self.name

#   def save_user(self):
#     self.save()

#   def delete_user(self):
#     self.delete()


class User(AbstractUser):
  username=models.CharField(max_length=250,unique=True)
  email=models.EmailField(unique=True)
  first_name=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

  REQUIRED_FIELD=[]

  def __str__(self):
    return str(self.first_name)

