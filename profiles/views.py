from django.shortcuts import render
from rest_framework import status

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Profile

from .serializers import ProfileSerializer
from django.http import Http404
# Create your views here.
class ProfileRetrieveAPIView(RetrieveAPIView):
  permission_classes = (AllowAny,)
  serializer_class = ProfileSerializer

  def retrieve(self, request, username, *args, **kwargs):
    try:
      profile = Profile.objects.select_related('user').get(
        user__username=username
      )
    except Profile.DoesNotExist:
      raise HTTP404()

    serializer = self.serializer_class(profile)

    return Response(serializer.data, status=status.HTTP_200_OK)
