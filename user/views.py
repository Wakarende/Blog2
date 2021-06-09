from django.shortcuts import render
from .serializers import RegistrationSerializer,LoginSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


# Create your views here.
class Registration(APIView):
  serializer_class=RegistrationSerializer

  def post(self, request):
    serializer=self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

            user_data=serializer.data

            response={
                "data":{
                    "user":dict(user_data),
                    "status":"Success",
                    "message":"User account created successfully"
                }

            }
            return Response(response, status=status.HTTP_201_CREATED)

        def get(self,request,format=None):
            users= User.objects.all()
            serializers=RegistrationSerializer(users, many=True)
            return Response(serializers.data)
