from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProcessPayment
from rest_framework import status
from .utils import validate_date, payment_gateway, checkLuhn
from .serializers import ProcessPaymentSerializer
import traceback
# Create your views here.
class ProcessPaymentView(APIView):
    model = ProcessPayment
    queryset = ProcessPayment.objects.all()
    serializer_class = ProcessPaymentSerializer

    # def get(self, request, format=None):
    #     """
    #     Return a list of all payments.
    #     """
    #     try:
    #         serializer = self.serializer_class(self.queryset.all(), many=True)
    #         context = {"success": True, "message": "Payment List", "error": "", "data": serializer.data}
    #         return Response(context, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(traceback.format_exc())
    #         context = {'error': str(e), 'success': "false",
    #                    'message': 'Failed to get Payment List.'}
    #         return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        """
        Processes a new payment and stores the details.
        """
        try:
            if request.data["credit_card_number"] == '' or request.data["card_holder"] == '' or request.data["expiration_date"] == '' or  request.data["amount"] == '':
                context = {"success": False, "message": "Invalid Input Data to process payment"}
                return Response(context, status=status.HTTP_400_BAD_REQUEST)


            is_credit_card_valid = checkLuhn(request.data['credit_card_number'].replace(" ", ""))
            # is_credit_card_valid = validate_credit_card(request.data['credit_card_number'].replace(" ", ""))
            if is_credit_card_valid == False:
                context = {"success": False, "message": "Invalid Credit Card Number"}
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
            is_date_valid = validate_date(request.data['expiration_date'])
            if is_date_valid == False:
                context = {"success": False, "message": "Your credit Card has Expired", }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)

            payment_gateway_used = payment_gateway(request.data['amount'])
            
            # serializer = self.serializer_class(data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            data = {
                # "request_data" : request.data,
                "credit_card_number": request.data['credit_card_number'],
                "card_holder": request.data['card_holder'],
                "expiration_date": request.data['expiration_date'],
                "security_code": request.data['security_code'],
                "amount": request.data['amount'],
                "is_credit_card_valid" : is_credit_card_valid,
                "is_date_valid" : is_date_valid,
                "payment_gateway" : payment_gateway_used
            }
            context = {"success": True, "message": "Payment Processed Successfully", "error": "" ,"data": data}
            return Response(context, status=status.HTTP_200_OK)
            # context = {"success": False, "message": "Invalid Input Data to process payment", "error": str(serializer.errors)}
            # return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            context = {'error': str(error), 'success': "false", 'message': 'Failed to process payment.'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
