from rest_framework import serializers
from .models import User
# from django.contrib.auth.models import User
from blogs.serializers import ArticleSerializer

# class ProfileSerializer(serializers.ModelSerializer):
#     article=ArticleSerializer(many=True, read_only=True)
#     class Meta:
#       model = Profile


      
# class RegistrationSerializer(serializers.ModelSerializer):
#   username=serializers.CharField()
#   email=serializers.EmailField()
#   password=serializers.CharField(
#     min_length=8,
#     max_length=20,
#     write_only=True,
#     error_messages={
#       "min_length": "Password should be atleast {min_length} characters"
#     }

#   )
#   confirmpassword=serializers.CharField(
#     min_length=8,
#     max_length=20,
#     write_only=True,
#     error_messages={
#       "min_length": "Password should be atleast {min_length} characters"
#     }
#   )

#   class Meta:
#     model=User
#     fields=["username", "email", "password", "confirmpassword"]

#   def create(self, validated_data):
#     user=User.objects.create(
#       username=validated_data['username'],
#       email=validated_data['email']
#     )
#     user.set_password(validated_data['password'])
#     user.save()
#     return user

# class LoginSerializer(serializers.ModelSerializer):
#   username=serializers.CharField()
#   password=serializers.CharField(
#     min_length=8,
#     max_length=20,
#     write_only=True,
#     error_messages={
#       "min_length": "Password should be atleast {min_length} characters"
#     }

#   )
#   class Meta:
#     model=User
#     fields=["username", "password"]

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username','email', 'password']
    extra_kwargs = {
      'password': {'write_only': True, }
    }

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance





