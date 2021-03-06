from django.db import models
from django.utils.translation import gettext_lazy as _
import secrets

from .payment_gateway import PayStack #FlutterWave

class Payment (models.Model):
    """
    payment data stored and their ref.
    """
    amount = models.PositiveIntegerField(
        verbose_name = _('Amount to be paid'),
        null=True, 
        help_text=_('Amount to be paid for the followiing action.')
        )
    ref = models.CharField(
        verbose_name = _('Payment Reference Number'),
        max_length = 500,
        null=True,
        help_text = _('Reference number of the the above payment')
        )
    email = models.EmailField(
        verbose_name = _('Email of the customer'),
        null=True,
        help_text = _('Email address of the customer'),
    )

    verified = models.BooleanField(
        verbose_name = _('Verified Status'),
        null=True, default=False,
        help_text = _('Verified payment status to identify if the payment is been verified by the payment gateway or not.')
    )

    date_created = models.DateTimeField(
        verbose_name = _('Date of the payment'),
        auto_now_add=True,
        help_text=_("the date when the payment was taken place.")
    )

    #Metadata
    class Meta :
        ordering = ['-date_created']
        verbose_name=_('All Payment')
        verbose_name_plural=_('All Payment')

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(30)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 100 

    def verify_payment(self):
        paystack = PayStack()
        # flutterwave = FlutterWave()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True
            return False 
   
    def __str__(self):
        return str(self.amount)
