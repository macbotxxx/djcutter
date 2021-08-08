from .forms import PaymentForm
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            context = {
                'payment_form':payment_form,
            }
            return render(request, 'pages/home.html', context)
    else:
        payment_form = PaymentForm()
        context = {
            'payment_form':payment_form,
        }
    return render(request, 'pages/home.html', context)
