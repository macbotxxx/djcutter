from .models import Payment
from django.contrib import admin


@admin.register(Payment)
class PaymentAdmin (admin.ModelAdmin):
    list_display = ('amount', 'ref', 'verified', 'date_created')
    list_display_links = ('amount', 'ref', 'verified', 'date_created')
