from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('',views.initiate_payment, name='home'),
    path('',views.initiate_payment, name='about'),
    path('<str:ref>/',views.verify_payment, name='verify-payment'),
    ]