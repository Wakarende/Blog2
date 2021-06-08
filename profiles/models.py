from django.db import models
from cloudinary.models import CloudinaryField
from django.db import models
from core.models import TimestampedModel


# Create your models here.
class Profile(TimestampedModel):
  user = models.OneToOneField(
    'authentication.User', on_delete=models.CASCADE
  )
  bio = models.TextField(blank=True)
  image = CloudinaryField('profile picture',blank=True)


  def __str__(self):
    return self.user.username






