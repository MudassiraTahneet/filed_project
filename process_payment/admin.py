from django.contrib import admin

from .models import ProcessPayment, PaymentGateway

class ProcessPaymentAdmin(admin.ModelAdmin):
    list_display = ('id','credit_card_number', 'card_holder', 'expiration_date',)
    search_fields = ('id','credit_card_number', 'card_holder','expiration_date',)   

admin.site.register(ProcessPayment, ProcessPaymentAdmin)

class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')

admin.site.register(PaymentGateway, PaymentGatewayAdmin)