from django.db import models
from django.db import models
from model_utils.models import TimeStampedModel
from pedidos.models import Pedido


class Pago(TimeStampedModel):
    pedido = models.ForeignKey(Pedido, related_name="pagos", on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(
        "Valor de la transacción", max_digits=10, decimal_places=2
    )
    installments = models.IntegerField("Cuotas")
    payment_method_id = models.CharField("Método de Pagamento", max_length=250)
    email = models.EmailField()
    doc_number = models.CharField("Documento de pago",max_length=20)
    # LOS SIGUIENTES CAMPOS SON DE RESPUESTA PUEDEN IR APARTE
    mercado_pago_id = models.CharField(max_length=250, blank=True, db_index=True)
    mercado_pago_status = models.CharField(max_length=250, blank=True)
    mercado_pago_status_detail = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ("-modified",)

    def __str__(self):
        return f"Pago {self.id}"
