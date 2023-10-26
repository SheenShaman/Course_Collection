from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentsListAPIView

app_name = PaymentsConfig.name

urlpatterns = [
    path('payment/', PaymentsListAPIView.as_view(), name='payment-list'),
]
