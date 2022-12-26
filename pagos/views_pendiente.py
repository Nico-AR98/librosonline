from productos.models.producto import Producto
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q
from usuario.models import Perfil
from django.contrib.sites.models import Site
from pedidos.models import Pedido
from pedidos.models import Item

 
class PagoPendiente(View):
    template = "pagos/pendiente.html"

    def get(self, request):
        params = {}

        # ##########################################################
        # PARA USUARIO
        # ###########################################################
        if request.user.is_authenticated:
            pedidos = Pedido.objects.filter(Q(usuario=request.user))
            print(pedidos)
            params["pedidos"] = pedidos
            params["usuario"] = request.user
            try:
                datos_para_imagen = Perfil.objects.get(usuario=request.user.pk)
                params["datos_para_imagen"] = datos_para_imagen
            except ObjectDoesNotExist:
                pass
        # ##########################################################
        # PARA RUTAS EN LINKS
        # ###########################################################
        current_site = Site.objects.get_current()
        params["dominio_actual"] = current_site.domain
        return render(request, self.template, params)