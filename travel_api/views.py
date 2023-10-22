import datetime
import random

from TravelAgency_API import settings
from liqpay.liqpay3 import LiqPay
from django.db.models import Count, F
from django.core.exceptions import FieldError
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

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
    serializer_class = TourSerializer
    pagination_class = TourPagination
    ordering_fields = ['name', 'free_places', 'price', 'date_start']
    ordering = ['name', 'free_places']

    def get_queryset(self):
        queryset = Tour.objects.all().order_by(*self.ordering)

        seasons = self.request.query_params.getlist('season', [])
        if seasons:
            queryset = queryset.filter(season__name__in=seasons)
        durations = self.request.query_params.getlist('duration', [])
        if durations:
            queryset = Tour.objects.filter(
                date_end__in=[F('date_start') + datetime.timedelta(days=int(dur)) for dur in durations])

        ordering = self.request.query_params.get('ordering', '')
        if ordering:
            try:
                queryset = queryset.order_by(ordering)
            except FieldError:
                return _Response({'error': 'Sorting by incorrect field'})

        return queryset


class TourSearch(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    pagination_class = TourPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']


class FeaturedTours(generics.ListAPIView):
    queryset = Tour.objects.filter(is_featured=True)

    def get(self, request, **kwargs):
        queryset = Tour.objects.filter(is_featured=True)
        sorted_query = queryset.annotate(order_count=Count('order')).order_by('-order_count')
        paginator = TourPagination()

        page = paginator.paginate_queryset(sorted_query[:4], request=request)

        return paginator.get_paginated_response(FeaturedSerializer(page, many=True).data)


class DetailsTour(APIView):
    def get(self, request, id):
        queryset = Tour.objects.get(id=id)

        return Response(DetailsSerializer(queryset, many=False).data)


class PayView(TemplateView):
    template_name = 'billing/pay.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
             'action': 'pay',
             'amount': 1,
             'currency': 'UAH',
             'description': 'Payment for test',
             'order_id': 'tes_id_10',
             'version': '3',
             'sandbox': 1,  # sandbox mode, set to 1 to enable it
             'server_url': 'http://127.0.0.1:8000/pay-callback/',  # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        html = liqpay.cnb_form(params)

        return render(request, self.template_name, {'signature': signature, 'data': data})


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.GET.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(f"{settings.LIQPAY_PRIVATE_KEY} + {data} + {settings.LIQPAY_PRIVATE_KEY}")
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)

        payment_status = liqpay.api("request", {
            "action": "status",
            "version": "3",
            "order_id": response['order_id']
        })
        return Response(payment_status)


class OrderPaymentView(APIView):
    def post(self, request, tour_id):
        request.data['tour_id'] = tour_id
        queryset = Tour.objects.get(id=request.data['tour_id'])
        final_cost = queryset.price * len(request.data['name'])
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': final_cost,
            'currency': 'UAH',
            'description': f'{queryset.name} - {len(request.data["name"])} passengers',
            'order_id': random.randint(100000, 999999),
            'version': '3',
            'sandbox': 0,  # sandbox mode, set to 1 to enable it
            'server_url': 'http://127.0.0.1:8000/pay-callback/',  # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return Response({"data": data, "signature": signature})
