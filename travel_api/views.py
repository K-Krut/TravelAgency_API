from django.shortcuts import render
from django.forms import model_to_dict
from django.shortcuts import render
from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import generics
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
            try:
                queryset = Tour.objects.order_by(request.query_params['sort'])
                page = paginator.paginate_queryset(queryset, request=request)
                return paginator.get_paginated_response(TourSerializer(page, many=True).data)
            except:
                page = paginator.paginate_queryset(queryset, request=request)
                return paginator.get_paginated_response(TourSerializer(page, many=True).data)


class TourSearch(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    pagination_class = TourPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']


class FeaturedTours(generics.ListAPIView):
    def get(self, request, **kwargs):
        queryset = Tour.objects.filter(is_featured=True)
        sorted_query = queryset.annotate(order_count=Count('order')).order_by('-order_count')
        paginator = TourPagination()

        page = paginator.paginate_queryset(sorted_query[:4], request=request)

        return paginator.get_paginated_response(FeaturedSerializer(page, many=True).data)


class DetailsTour(APIView):
    def get(self, request):
        a = Tour.objects.get(id=5)
        return Response(DetailsSerializer(a, many=False).data)