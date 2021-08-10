from .forms import PaymentForm
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.contrib import messages
from .models import Payment

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            context = {
                'payment':payment,
                'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
                'flutterwave_public_key': settings.FLUTTERWAVE_PUBLIC_KEY,
            }
            return render(request, 'pages/about.html', context)
    else:
        payment_form = PaymentForm()
        context = {
            'payment_form':payment_form,
        }
    return render(request, 'pages/home.html', context)


def verify_paymentx (request, ref):
    payment = Payment.objects.filter(ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'payment verified')
    else:
        messages.error(request, 'payment verified failed')

    return redirect('home')

