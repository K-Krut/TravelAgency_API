from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class ToursList(generics.ListCreateAPIView):
    queryset = Tour.objects.order_by("name", "free_places")
    serializer_class = TourSerializer
