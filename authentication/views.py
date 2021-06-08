from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

from .serializers import RegistrationSerializer
# from .renderers import UserJSONRenderer

# Create your views here.
class RegistrationAPIView(APIView):
  permission_classes = [AllowAny,]
  serializer_class = RegistrationSerializer
  # renderer_classes = (UserJSONRenderer,)

  def post(self, request,format=None):
    # user = request.data.get(User, {})
    user = request.data
    print(user)
    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def get(self,request, *args, **kwargs):
    serializer=self.serializer_class(User.objects.all(),many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)