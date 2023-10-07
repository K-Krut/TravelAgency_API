from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class TourPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10


class ToursList(generics.ListCreateAPIView):
    queryset = Tour.objects.order_by("name", "free_places")
    serializer_class = TourSerializer
    pagination_class = TourPagination

    def get(self, request, **kwargs):
        queryset = Tour.objects.all()
        paginator = TourPagination()

        if len(request.query_params) == 0:
            page = paginator.paginate_queryset(queryset, request=request)
            return paginator.get_paginated_response(TourSerializer(page, many=True).data)
        else:
            queryset = Tour.objects.order_by(request.query_params['sort'])
            page = paginator.paginate_queryset(queryset, request=request)
            return paginator.get_paginated_response(TourSerializer(page, many=True).data)
