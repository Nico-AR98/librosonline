from django.urls import path
from pagos.views_costo_envio import CostoEnvioView
from pagos.views_crear import PagoCrearView
from pagos.views_fallido import PagoFallido
from pagos.views_pendiente import PagoPendiente
from pagos.views_exitoso import PagoExitoso
from pagos.views_webhook import pago_webhook


urlpatterns = [
    path("costo_envio", CostoEnvioView.as_view(), name="costo_envio"),
    path("", PagoCrearView.as_view(), name="process"),
    path("failure", PagoFallido.as_view(), name="failure"),
    path("pending", PagoPendiente.as_view(), name="pending"),
    path("success", PagoExitoso.as_view(), name="success"),
    path("webhook", pago_webhook, name="webhook"),
]
