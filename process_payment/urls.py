from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'process_payment'

urlpatterns = [
    path('', ProcessPaymentView.as_view(),name='process-payment')
]