
def checkLuhn(cardNo):
     
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False

# def validate_credit_card(l):
#     lst=[]
#     for d in l:
#         lst.append(d)
#     if len(lst) == 16:
#         for i in range(0, len(lst)):
#             lst[i] = int(lst[i])
#         last = lst[15]
#         first = lst[:15]
#         first = first[::-1]
#         for i in range(len(first)):
#             if i % 2 == 0:
#                 first[i] = first[i] * 2
#             if first[i] > 9:
#                 first[i] -= 9
#         sum_all = sum(first)
#         t1 = sum_all % 10
#         t2 = t1 + last
#         if t2 % 10 is 0:
#             return True
#         else:
#             return False
#     else:
#         return False

import datetime

def validate_date(given_date_str):
    given_date = datetime.datetime.strptime(given_date_str, '%Y-%m-%d %H:%M:%S')
    today = datetime.datetime.today()
    if given_date >= today:
        return True
    else:
        return False

from .models import PaymentGateway
def payment_gateway(amt):
    amt = float(amt)
    if amt <= 20:
        try:
            return PaymentGateway.objects.get(id=4).name
        except:
            return 'CheapPaymentGateway'

    elif amt>20 and amt<=500:
        try:
            return PaymentGateway.objects.get(id=2).name
        except:
            return 'ExpensivePaymentGateway'
    else:
        try:
            return PaymentGateway.objects.get(id=1).name
        except:
            return 'PremiumPaymentGateway'
