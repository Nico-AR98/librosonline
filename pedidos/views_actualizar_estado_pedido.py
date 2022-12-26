import json
from django.http import HttpResponse
from pedidos.models import Pedido
from django.db.models import Q
from productos.models.producto import Producto
from pedidos.models import Item


def actualizar_estado_pedido(request, *args, **kwargs):
    if request.method == "GET":
        probar_pedido = Pedido.objects.get(
            Q(usuario=request.user), Q(estado="A CONFIRMAR")
        )
        probar_pedido.estado = "ACREDITADO"
        probar_pedido.save()
        articulos_actualizar_stock = Item.objects.filter(pedido=probar_pedido)
        for art in articulos_actualizar_stock:
            articulo = Producto.objects.get(
                articulo=art.articulo, talle=art.talle, color=art.color
            )
            print(articulo)
            articulo.stock = int(articulo.stock) - int(art.cantidad)
            articulo.save()
        results = []
        data = {}
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)