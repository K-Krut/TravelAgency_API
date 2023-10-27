import random
from django.http import JsonResponse
from TravelAgency_API import settings
from liqpayapi.liqpay3 import LiqPay
from django.db.models import Count, F
from django.core.exceptions import FieldError
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from rest_framework import filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import *
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
                return Response({'error': 'Sorting by incorrect field'})

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
        return render(request, self.template_name, {
            'signature': request.GET.get('signature'),
            'data': request.GET.get('data')
        })


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        response = get_liqpay_decoded_response(request)
        print('callback data', response)

        payment_status = get_liqpay_payment_status(response)
        if payment_status.get('status') == "error":
            send_payment_error_email(response, payment_status)
            return JsonResponse(payment_status)

        order = update_order(payment_status)
        order_response = get_order_response(order, response)
        send_mail_("Admin, було сформовано нове замовлення",
                   create_message(order, order_response))
        # except Exception as e:
        #     send_mail_("Error - ошибка при создании заказа",
        #                f"Данные оплаты: {response}\n\nОшибка: {e}")
        #     response_for_user = JsonResponse({"Error": "Ошибка при создании заказа"})
        return JsonResponse(order_response)


class OrderPaymentView(APIView):
    def post(self, request, tour_id):
        request.data['tour_id'] = tour_id
        tour = Tour.objects.get(id=request.data['tour_id'])
        final_cost = tour.price * len(request.data['passengers'])
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        code = random.randint(100000, 999999)

        order = Order.objects.create(
            tour=tour,
            sum=final_cost,
            sum_paid=0,
            code=code,
            status=OrderStatus.objects.get(id=10),
            paytype='pay'
        )

        for passenger in request.data['passengers']:
            print(passenger)
            place_number = tour.free_places - 1
            print(request.data)

            create_order(
                order,
                place_number,
                passenger['name'],
                passenger['surname'],
                passenger.get("phone", ""),
                tour.price,
                passenger.get('is_primary_contact', False),
                code
            )

        params = {
            'action': 'pay',
            'amount': final_cost,
            'currency': 'UAH',
            'description': f'{tour.name} - {len(request.data["passengers"])} passengers',
            'order_id': code,
            'version': '3',
            'sandbox': 1,
            'server_url': 'http://127.0.0.1:8000/pay-callback/',
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)

        return Response({"data": data, "signature": signature})
