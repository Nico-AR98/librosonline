import json
from django.http import HttpResponse
from django.db.models import Q
from pedidos.models import Pedido
from transporte.models import PreciosRIDomicilio
from transporte.models import PreciosMCFDomicilio

def ver_peso(var):
    peso_t = 0
    if var <= 0.5:
        print("es menor a 0.5")
        peso_t = 0.5
        print(peso_t)
        return peso_t
    elif var > 0.5 and var <= 1:
        print("valor entre 0.5 y 1")
        peso_t = 1
        print(peso_t)
        return peso_t
    elif var > 1 and var <= 2:
        print("valor entre 1 y 2")
        peso_t = 2
        print(peso_t)
        return peso_t
    elif var > 2 and var <= 3:
        print("valor entre 2 y 3")
        peso_t = 3
        print(peso_t)
        return peso_t
    elif var > 3 and var <= 5:
        print("valor entre 3 y 5")
        peso_t = 5
        print(peso_t)
        return peso_t
    elif var > 5 and var <= 10:
        print("valor entre 5 y 10")
        peso_t = 10
        print(peso_t)
        return peso_t
    elif var > 10 and var <= 15:
        print("valor entre 10 y 15")
        peso_t = 15
        print(peso_t)
        return peso_t
    elif var > 15 and var <= 20:
        print("valor entre 15 y 20")
        peso_t = 20
        print(peso_t)
        return peso_t
    elif var > 20 and var <= 25:
        print("valor entre 20 y 25")
        peso_t = 25
        print(peso_t)
        return peso_t
    else:
        print("peso fuera de rango")
        peso_t = 100
        print(peso_t)
        return peso_t


def determinar_zona(var):
    if (
        var == "Buenos Aires"
        or var == "Capital Federal"
        or var == "Córdoba"
        or var == "Entre Ríos"
        or var == "La Pampa"
        or var == "Santa Fe"
    ):
        return "zona_2"
    elif (
        var == "Catamarca"
        or var == "Chaco"
        or var == "Corrientes"
        or var == "Formosa"
        or var == "La Rioja"
        or var == "Mendoza"
        or var == "Misiones"
        or var == "Neuquén"
        or var == "Río Negro"
        or var == "San Juan"
        or var == "San Luis"
        or var == "Santiago del Estero"
        or var == "Tucumán"
    ):
        return "zona_3"
    elif (
        var == "Chubut"
        or var == "Jujuy"
        or var == "Salta"
        or var == "Santa Cruz"
        or var == "Tierra del Fuego"
    ):
        return "zona_4"


def correo_argentino(request, *args, **kwargs):
    if request.method == "GET":
        enviar = request.GET.get("enviar")

        # ###########################################
        #
        # ###########################################
        el_pedido = Pedido.objects.filter(
            Q(usuario=request.user), Q(estado="A CONFIRMAR")
        ).latest("id")
        total = float(el_pedido.total)

        print("AAAAAAAAAAAAAAAAAAA")
        # print(el_pedido.get_total_price())
        el_peso = el_pedido.get_peso_total()
        print(type(el_peso))
        ver_peso(el_peso)
        # print(enviar)

        # print(total + )
        print("BBBBBBBBBBBBBBBBBBB")
        if enviar == "retirar_fabrica":
            enviar = enviar
            total = total
            total_mas_e = total
            tipo_transporte = "EN FABRICA"
        elif enviar == "envio_ri":
            enviar = enviar
            print(el_pedido.provincia)
            zona = determinar_zona(el_pedido.provincia)
            print(zona)
            tipo_transporte = "A DOMICILIO"
            # ACTUALIZAR PRECIO 1
            if zona == "zona_2":
                actualizar_precio = PreciosRIDomicilio.objects.filter(
                    Q(peso=ver_peso(el_peso))
                )
                for act in actualizar_precio:
                    print(act.zona_2)
                    total_mas_e = total + float(act.zona_2)
                    total_mas_e = "{0:.2f}".format(total_mas_e)

                print(total)
            if zona == "zona_3":
                actualizar_precio = PreciosRIDomicilio.objects.filter(
                    Q(peso=ver_peso(el_peso))
                )
                for act in actualizar_precio:
                    print(act.zona_3)
                    total_mas_e = total + float(act.zona_3)
                    total_mas_e = "{0:.2f}".format(total_mas_e)
                print(total)
            if zona == "zona_4":
                actualizar_precio = PreciosRIDomicilio.objects.filter(
                    Q(peso=ver_peso(el_peso))
                )
                for act in actualizar_precio:
                    print(act.zona_4)
                    total_mas_e = total + float(act.zona_4)
                    total_mas_e = "{0:.2f}".format(total_mas_e)
                print(total)
        elif enviar == "envio_mon":
            enviar = enviar
            print(el_pedido.provincia)
            zona = determinar_zona(el_pedido.provincia)
            print(zona)
            tipo_transporte = "A DOMICILIO"
            # ACTUALIZAR PRECIO 1
            if zona == "zona_2":
                actualizar_precio = PreciosMCFDomicilio.objects.filter(
                    Q(peso=ver_peso(el_peso))
                )
                for act in actualizar_precio:
                    print(act.zona_2)
                    total_mas_e = total + float(act.zona_2)
                    total_mas_e = "{0:.2f}".format(total_mas_e)
                print(total)
            if zona == "zona_3":
                actualizar_precio = PreciosMCFDomicilio.objects.filter(
                    Q(peso=ver_peso(el_peso))
                )
                for act in actualizar_precio:
                    print(act.zona_3)
                    total_mas_e = total + float(act.zona_3)
                    total_mas_e = "{0:.2f}".format(total_mas_e)
                print(total)
            if zona == "zona_4":
                actualizar_precio = PreciosMCFDomicilio.objects.filter(
                    Q(peso=ver_peso(el_peso))
                )
                for act in actualizar_precio:
                    print(act.zona_4)
                    total_mas_e = total + float(act.zona_4)
                    total_mas_e = "{0:.2f}".format(total_mas_e)
                print(total)
        elif enviar == "coordinar_fa":
            enviar = enviar
            total_mas_e = total
            tipo_transporte = "A COORDINAR"
        el_pedido = Pedido.objects.filter(
            Q(usuario=request.user), Q(estado="A CONFIRMAR")
        ).latest("id")
        el_pedido.total_mas_envio = total_mas_e
        el_pedido.tipo_transporte = "A COORDINAR"
        el_pedido.save()

        print("CCCCCCCCCCCCCCCCCCCC")
        # ###########################################
        #
        # ###########################################

        results = []
        data = {}
        data["enviar"] = enviar
        data["total"] = total
        data["total_mas_e"] = total_mas_e
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
