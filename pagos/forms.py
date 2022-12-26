import mercadopago
from django import forms
from django.conf import settings
from .models import Pago

class PagoForm(forms.ModelForm):
    token = forms.CharField()

    class Meta:
        model = Pago
        fields = [
            "transaction_amount",
            "installments",
            "payment_method_id",
            "email",
            "doc_number",
        ]

    def __init__(self, *args, **kwargs):
        # ****************************************************
        # Valor de pedido recibido desde view_crear.pedido()
        # ****************************************************
        self.pedido = kwargs.pop("pedido")
        print("Valor del pedido pasado al formulario: ", self.pedido)
        super().__init__(*args, **kwargs)

    def save(self):
        cd = self.cleaned_data
        mp = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
        print(mp)
        payment_data = {
            "transaction_amount": float(self.pedido.total_mas_envio),
            "token": cd["token"],
            "description": self.pedido.get_description(),
            "installments": cd["installments"],
            "payment_method_id": cd["payment_method_id"],
            "payer": {
                "email": cd["email"],
                "identification": {"type": "DNI", "number": cd["doc_number"]},
            },
        } 
        payment = mp.payment().create(payment_data)  #Respuesta de mercado pago
        print(payment)

        if payment["status"] == 201:     #201 si pago creado
            self.instance.pedido = self.pedido
            self.instance.mercado_pago_id = payment["response"]["id"]
            self.instance.mercado_pago_status_detail = payment["response"][
                "status_detail"
            ]
            self.instance.mercado_pago_status = payment["response"]["status"]
            if payment["response"]["status"] == "approved":
                self.pedido.estado = "ACREDITADO"
                self.pedido.save()               
            self.instance.save()    
        
# Actualiza el pago
class UpdatePagoForm(forms.Form):
    action = forms.CharField()
    data = forms.JSONField()
    print("*********************************")
    print(action)
    print(data)
    print("*********************************")
    # SI EL FORMULARIO ES VÁLIDO SE LLAMA A ESTE SAVE()
    def save(self):
        cd = self.cleaned_data
        mp = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
        print(mp)
        if cd["action"] == "payment.updated":
            mercado_pago_id = cd["data"]["id"]
            payment = Pago.objects.get(mercado_pago_id=mercado_pago_id)   #valor de pago de mi base de datos
            payment_mp = mp.payment().get(mercado_pago_id)                #valor de pago desde mercado pago  
            payment.mercado_pago_status = payment_mp["response"]["status"]
            payment.mercado_pago_status_detail = payment_mp["response"]["status_detail"]
            if payment_mp["response"]["status"] == "approved":
                payment.pedido.estado = "ACREDITADO"
            else:
                payment.pedido.estado = "NO ACREDITADO"
            payment.pedido.save()
            payment.save()
