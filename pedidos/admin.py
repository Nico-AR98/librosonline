from django.contrib import admin
from pedidos.models import Pedido
from pedidos.models import Item
from pedidos.models import EnviarFactura
from pagos.models import Pago


class ItemInline(admin.TabularInline):

    model = Item
    raw_id_fields = ["cada_producto"]  #esto es porque no quiero una lista de productos, solo el id del producto
    extra = 0
    """readonly_fields = [
        "usuario",
        "producto",
        "cantidad",
        "precio",
         
    ]"""

    def has_change_permission(self, request, obj=None):
        return False

class EnviarFacturaInline(admin.TabularInline):

    model = EnviarFactura
    extra = 0


class PagoInline(admin.TabularInline):
    model = Pago
    can_delete = False
    readonly_fields = (
        "email",
        "doc_number",
        "transaction_amount",
        "installments",
        "payment_method_id",
        "mercado_pago_id",
        "mercado_pago_status",
        "mercado_pago_status_detail",
        "modified",
    )
    ordering = ("-modified",)

    def has_add_permission(self, request, obj):
        return False


class Pedidoadmin(admin.ModelAdmin):

 
    fieldsets = [
        (
            "Datos del pedido",
            {
                "fields": [
                    "tipo_transporte",
                    "referencia",
                    "estado_de_pedido",
                    "total",
                    "total_mas_envio",
                    "created",
                    "modified",
                ]
            },
        ),
        (
            "Datos del comprador",
            {
                "fields": [
                    "usuario",
                    "documento",
                    "email",
                    "nombre",
                    "apellido",
                    "domicilio",
                    "provincia",
                    "localidad",
                    "codigo_postal",
                    "telefono",
                    "mensaje",
                ]
            },
        ),
        (
            "Datos del Destinatario",
            {
                "fields": [
                    "nombre_apellido_recibe",  
                    "documento_recibe",  
                    "domicilio_recibe", 
                    "localidad_recibe", 
                    "provincia_recibe",
                    "codigo_postal_recibe", 
                    "telefono_recibe",
                ]
            },
        ),

        (
            "Factura A / E",
            {
                "fields": [
                    "cuil_cuit",
                    "condicion_afip",
                    "razon_social",
                    "domicilio_comercial",
                ]
            },
        ),   
    ]
    list_display = [
        "tipo_transporte",
        "referencia",
        "estado_de_pedido",
        "total",
        "total_mas_envio",
        "usuario",
        "nombre",
        "apellido",
        "cuil_cuit",
        "domicilio",
        "provincia",
        "localidad",
        "codigo_postal",
        "telefono",
        "documento",
        "mensaje",
        # "fecha",
        "email",
        "created",
        "modified",
    ]
    readonly_fields = [
        #"cada_producto",
        "tipo_transporte",
        "referencia",
        "estado_de_pedido",
        "total",
        "total_mas_envio",
        "usuario",
        "nombre",
        "apellido",
        "cuil_cuit",
        "condicion_afip",
        "razon_social",
        "domicilio_comercial",
        "documento",
        "domicilio",
        "provincia",
        "localidad",
        "codigo_postal",
        "telefono",
        "documento",
        "mensaje",
        # "fecha",
        "email",
        "created",
        "modified",
        "nombre_apellido_recibe",  
        "documento_recibe",  
        "domicilio_recibe", 
        "localidad_recibe", 
        "provincia_recibe",
        "codigo_postal_recibe", 
        "telefono_recibe",


    ]

    list_filter = [
        "estado",
        "created",
        "modified",
    ]  # "fecha"

    search_fields = ["nombre", "email", "documento"]
    inlines = [ItemInline, PagoInline, EnviarFacturaInline]
    actions = ["pedido_enviado"]

    def pedido_enviado(self, request, queryset):
        queryset.update(estado="DESPACHADO")

    pedido_enviado.short_description = "Despachado"


admin.site.register(Pedido, Pedidoadmin)