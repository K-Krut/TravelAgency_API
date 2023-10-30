from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from travel_api import views

urlpatterns = [
    path('tours', views.ToursList.as_view()),
    path('tours/', views.TourSearch.as_view()),
    path('tours/featured', views.FeaturedTours.as_view()),
    path('tours/<int:id>/', views.DetailsTour.as_view()),

    path('tours/<int:tour_id>/order/payment', views.OrderPaymentView.as_view()),
    path(r'pay', views.PayView.as_view(), name='pay_view'),
    path(r'pay-callback', views.PayCallbackView.as_view(), name='pay_callback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
