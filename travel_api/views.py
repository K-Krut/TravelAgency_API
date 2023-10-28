import random
from django.http import JsonResponse
from TravelAgency_API import settings
from TravelAgency_API.settings import BASE_URL
from liqpayapi.liqpay3 import LiqPay
from django.db.models import Count, F
from django.core.exceptions import FieldError, ObjectDoesNotExist
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
        tour = Tour.objects.get(id=id)
        try:
            return JsonResponse(DetailsSerializer(tour, many=False).data)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Tour not found'}, status=404)
        except TimeoutError:
            return JsonResponse({'error': 'Request timeout'}, status=503)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

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
        # try:
        response = get_liqpay_decoded_response(request)
        print(response)
        payment_status = get_liqpay_payment_status(response)
        if payment_status.get('status') == "error":
            send_mail_(f"Помилка із замовленням №{response.get('order_id')}",
                       generate_order_bad_request_email(response, payment_status))
            print(payment_status)
            return JsonResponse({'error': payment_status}, status=402)
        try:
            order = update_order(payment_status)
            order_response = get_order_response(order, response)
        except Exception as e:
            send_mail_(f"#ERROR із замовленням №{response.get('order_id')}",
                       generate_order_server_error_email(response, payment_status))
            return JsonResponse({'error': str(e)}, status=500)
        send_mail_("Admin, було успішно сформовано нове замовлення", generate_order_successful_email(order_response))
        return JsonResponse(order_response)
        # except Exception as e:
        #     return JsonResponse({'error': str(e)}, status=400)


class OrderPaymentView(APIView):
    def post(self, request, tour_id):
        try:
            request.data['tour_id'] = tour_id
            tour = Tour.objects.get(id=request.data['tour_id'])
            if not check_order_cost(tour, request):
                return JsonResponse({'error': 'You are trying to pay with incorrect cost'}, status=400)
            try:
                order = create_new_order(tour, request)
                create_order_items(request, order, tour)
            except Exception as e:
                return JsonResponse({'error': 'Failed Order creation in DB. ' + str(e)}, status=500)

            signature, data = get_liqpay_pay_data(request, order, tour)
            return JsonResponse({"data": data, "signature": signature})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
