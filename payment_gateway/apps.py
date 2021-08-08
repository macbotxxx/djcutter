from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PaymentGatewayConfig(AppConfig):
    name = 'payment_gateway'
    verbose_name = _("All Payment")
