from django.views.generic import View
from django.shortcuts import render
from django.db.models import Q
from django.contrib.sites.models import Site
from pedidos.models import Pedido

def ver_peso(var):
    peso_t = 0
    if var <= 0.5:
        print("es menor a 0.5")
        peso_t = 0.5
        print(peso_t)
        return peso_t
    elif var >0.5 and var <= 1:
        print("valor entre 0.5 y 1")
        peso_t = 1
        print(peso_t)
        return peso_t
    elif var >1 and var <= 2:
        print("valor entre 1 y 2")
        peso_t = 2
        print(peso_t)
        return peso_t
    elif var >2 and var <= 3:
        print("valor entre 2 y 3")
        peso_t = 3
        print(peso_t)
        return peso_t
    elif var >3 and var <= 5:
        print("valor entre 3 y 5")
        peso_t = 5
        print(peso_t)
        return peso_t
    elif var >5 and var <= 10:
        print("valor entre 5 y 10")
        peso_t = 10
        print(peso_t)
        return peso_t
    elif var >10 and var <= 15:
        print("valor entre 10 y 15")
        peso_t = 15
        print(peso_t)
        return peso_t
    elif var >15 and var <= 20:
        print("valor entre 15 y 20")
        peso_t = 20
        print(peso_t)
        return peso_t
    elif var >20 and var <= 25:
        print("valor entre 20 y 25")
        peso_t = 25
        print(peso_t)
        return peso_t
    else:
        print("peso fuera de rango")
        peso_t = 100
        print(peso_t)
        return peso_t

class CostoEnvioView(View):
    template = "pagos/costo_envio.html"

    def get(self, request):
        params = {}
        id_pedido = self.request.session["pedido_id"]
        pedido_id = Pedido.objects.get(Q(id=id_pedido)) 
        pedido_id.total
        params["pedido_id_total"]=pedido_id.total

        # ###########################################
        # VER PESO DE PEDIDO
        # ###########################################
        el_peso = pedido_id.get_peso_total()
        rango_peso = ver_peso(el_peso)
        params["rango_peso"] = rango_peso 

        # ################"##########################################
        # PARA RUTAS EN LINKS
        # ###########################################################
        current_site = Site.objects.get_current()
        params["dominio_actual"] = current_site.domain

        return render(request, self.template, params)