from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['detail'] = 'Incorrect filtering parameter'

    return response


def create_liqpay_object(final_cost, queryset_name, passengers):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    params = {
        'action': 'pay',
        'amount': final_cost,
        'currency': 'UAH',
        'description': f'{queryset_name} - {passengers} passengers',
        'order_id': random.randint(100000, 999999),
        'version': '3',
        'sandbox': 0,  # sandbox mode, set to 1 to enable it
        'server_url': 'http://127.0.0.1:8000/pay-callback/',  # url to callback view
    }