from django.shortcuts import render
from django.forms import model_to_dict
from django.shortcuts import render
from django.db.models import Count

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


class TourSearch(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    pagination_class = TourPagination

    def get(self, request):
        try:
            paginator = TourPagination()

            if len(request.query_params) == 0:
                return Response({'error': 'Endpoint Error. Example: api/v1/tours/search?name={name}'})
            else:
                queryset = Tour.objects.filter(name=request.query_params['name'])
                page = paginator.paginate_queryset(queryset, request=request)
                return paginator.get_paginated_response(TourSerializer(page, many=True).data)
        except Exception as e:
            return Response({"error": str(e)})


class FeaturedTours(generics.ListAPIView):
    def get(self, request):
        queryset = Tour.objects.filter(is_featured=True)
        sorted_query = queryset.annotate(order_count=Count('order')).order_by('-order_count')
        paginator = TourPagination()

        page = paginator.paginate_queryset(sorted_query[:4], request=request)

        return paginator.get_paginated_response(FeaturedSerializer(page, many=True).data)


class DetailsTour(APIView):
    def get(self, request, id):
        queryset = Tour.objects.get(id=id)

        return Response(DetailsSerializer(queryset, many=False).data)