from rest_framework import generics
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer, PersonSerializer

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
