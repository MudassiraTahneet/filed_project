from django.db import models
from django.core.validators import MinValueValidator
from decimal import *
# Create your models here.

class PaymentGateway(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        """Unicode method to display Username in Admin."""
        return str(self.name)

    class Meta:
        """Information About the class."""

        verbose_name = "Payment Gateway"
        verbose_name_plural = "Payment Gateways"

class ProcessPayment(models.Model):
    """docstring for ProcessPayment."""
    credit_card_number = models.CharField(max_length=25, unique=True)
    card_holder = models.CharField(max_length=50)
    expiration_date = models.DateTimeField() # was asked for date time or required is only date
    security_code = models.CharField(max_length=3, blank=True, null=True)
    amount =  models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(Decimal('0.01'))])
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        """Unicode method to display Username in Admin."""
        return str(self.card_holder)

    class Meta:
        """Information About the class."""

        verbose_name = "Process Payment"
        verbose_name_plural = "Process Payments"
        permissions = (
            ("see_processpayment", "Can See Process Payments"),
        )
        # constraints = [
        #     models.CheckConstraint(check=models.Q(amount__gt=Decimal('0')), name='amount_gt_0'),
        # ]
