from django.urls import path
from pedidos.views_checkout import Checkout
from pedidos.views_exito import Exito
from pedidos.views_politica import PaginaPolitica
from pedidos import views_realizar_pedido
from pedidos import views_actualizar_estado_pedido
from pedidos.views_mis_pedidos import MisPedidos
from pedidos.views_perfil_paso1 import EditPerfilPaso1

urlpatterns = [
    path(
        "actualizar_estado_pedido/",
        views_actualizar_estado_pedido.actualizar_estado_pedido,
        name="actualizar_estado_pedido",
    ),
    path("checkout/", Checkout.as_view(), name="checkout"),
    #path("creado/", Creado.as_view(), name="creado"),
    path("exito/", Exito.as_view(), name="exito"),
    path("politica/", PaginaPolitica.as_view(), name="politica"),
    path(
        "realizar_pedido/",
        views_realizar_pedido.realizar_pedido,
        name="realizar_pedido",
    ),
    path("mis_pedidos/", MisPedidos.as_view(), name="mis_pedidos"),
    path("perfil_paso1/", EditPerfilPaso1.as_view(), name="perfil_paso1"),
]