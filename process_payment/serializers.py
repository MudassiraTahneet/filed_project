from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from process_payment.models import ProcessPayment



class ProcessPaymentSerializer(ModelSerializer):
    class Meta:
        model=ProcessPayment
        fields='__all__'