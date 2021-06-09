from django.shortcuts import render
from rest_framework import status

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer
from django.http import Http404
from .exceptions import ProfileDoesNotExist

# Create your views here.
class ProfileRetrieveAPIView(RetrieveAPIView):
  permission_classes = [AllowAny,]
  serializer_class = ProfileSerializer
  renderer_classes = [ProfileJSONRenderer,]

  def retrieve(self, request, username, *args, **kwargs):
    try:
      profile = Profile.objects.select_related('user').get(
        user__username=username
      )
    except Profile.DoesNotExist:
      raise ProfileDoesNotExist

    serializer = self.serializer_class(profile)

    return Response(serializer.data, status=status.HTTP_200_OK)
