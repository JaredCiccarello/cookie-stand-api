from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import CookieSerializer
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly


class CookieStandlist(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer

class CookieStandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer
# Create your views here.
