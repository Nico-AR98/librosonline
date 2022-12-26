from django.contrib import admin

"""
from pagos.models import Pago


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "pedido",
        "doc_number",
        "email",
        "transaction_amount",
        "mercado_pago_id",
        "mercado_pago_status",
        "mercado_pago_status_detail",
        "created",
        "modified",
    ]
    list_filter = ["mercado_pago_status", "modified"]
    search_fields = ["doc_number", "email", "mercado_pago_id"]
"""