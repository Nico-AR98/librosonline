from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import cached_property
from django.views.generic import CreateView
from pedidos.models import Pedido
from pagos.forms import PagoForm
from pagos.models import Pago


class PagoCrearView(CreateView):   
    
    model = Pago
    form_class = PagoForm
    
    @cached_property
    def pedido(self):
        # *********************************************************
        # 1) Primero obtengo el id de pedido 
        # *********************************************************
        pedido_id = self.request.session.get("pedido_id")
        pedido = get_object_or_404(Pedido, id=pedido_id)
        return pedido
  
    def get_form_kwargs(self):
        # *********************************************************
        # 2) Envia información al formulario, lo uso para agregar el pedido al formulario
        # 2.1) Tomo lo dtos de: form_kwargs = super().get_form_kwargs()
        # 2.2) Creo una clave para pasar el pedido recuperado en el método pedido()
        # *********************************************************
        form_kwargs = super().get_form_kwargs()
        print("------------ get_form_kwargs() ------------------------")
        print(form_kwargs)
        form_kwargs["pedido"] = self.pedido
        print(form_kwargs)
        return form_kwargs

    def form_valid(self, form):
        # *********************************************************
        # Si el formulario es valido, hace esto:
        # 3.1) Llama al método save() que se encuentra dentro del formulario PagoForm (línea 33)
        # 3.2) Redirecciona según la respuesta
        # Por defecto iría a failure a no ser que obtenga un status diferente
        # *********************************************************
        form.save()
        print("Aún estoy aquí podría ver los datos")
        redirect_url = "/pagos/failure"
        status = form.instance.mercado_pago_status
        print(status)
        if status == "approved":
            redirect_url = "/pagos/success"
        if status == "in_process":
            redirect_url = "/pagos/pending"
        if status and status != "rejected":
            del self.request.session["pedido_id"]
        return redirect(redirect_url)

    def get_context_data(self, **kwargs):
        # *********************************************************
        # 4) Enviar a la vista los datos de forma de que 
        # el javascript tenga a disposición los datos.
        # *********************************************************
        context = super().get_context_data(**kwargs)
        context["pedido"] = self.pedido
        context["publishable_key"] = settings.MERCADO_PAGO_PUBLIC_KEY
        return context
