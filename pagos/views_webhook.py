import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from pagos.forms import UpdatePagoForm
 
@csrf_exempt
@require_POST
def pago_webhook(request):
    # ************************************
    # Esta función es quien atrapa a la respuesta
    # que envia mercado pago y crea una instanca 
    # de la clase UpdatePagoForm con los datos recibidos
    # ************************************
    data = json.loads(request.body)
    form = UpdatePagoForm(data)
    if form.is_valid():
        form.save()

    return JsonResponse({})