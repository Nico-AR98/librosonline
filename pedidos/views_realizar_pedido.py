import json
from django.http import HttpResponse
from usuario.models import Perfil
import ast
import re
from pedidos.models import Pedido
from usuario.models import Perfil
from django.db.models import Q

def es_valido_cuit(cuit):
    """
    Funcion destinada a la validacion de CUIT
    """
    # Convertimos el valor a una cadena
    cuit = str(cuit)
    # Aca removemos guiones, espacios y puntos para poder trabajar
    cuit = cuit.replace("-", "")  # Borramos los guiones
    cuit = cuit.replace(" ", "")  # Borramos los espacios
    cuit = cuit.replace(".", "")  # Borramos los puntos
    # Si no tiene 11 caracteres lo descartamos
    if len(cuit) != 11:
        return False, cuit
    # Solo resta analizar si todos los caracteres son numeros
    if not cuit.isdigit():
        return False, cuit
    # Despues de estas validaciones podemos afirmar
    #   que contamos con 11 numeros
    # Aca comienza la magia
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux % 11)
    if aux == 11:
        aux = 0
    elif aux == 10:
        aux = 9
    if int(cuit[10]) == aux:
        return True, cuit
    else:
        return False, cuit


def realizar_pedido(request, *args, **kwargs):
    if request.method == "GET":
        # ################################################################
        # TOMAR LOS DATOS Y CONVERTIR EL FORMATO.
        # ################################################################
        datos_pedido = request.GET
        datos_pedido_diccionario = datos_pedido.dict()
        datos_pedido_dict = ast.literal_eval(datos_pedido_diccionario["pedido"])
        print(datos_pedido_dict)
        # ################################################################
        # CHEQUEAR SI EL USUARIO ES MAYORISTA O NO
        # ###############################################################
        usuario = request.user
        clave_mayorista = ClaveMayorista.objects.last()
        clave_m = clave_mayorista.clave
        clave_mayorista_usuario = Perfil.objects.get(usuario=usuario)
        clave_mp = clave_mayorista_usuario.clave
        if clave_m == clave_mp:
            clave = "mayorista"
        else:
            clave = "minorista"
        # ################################################################
        # PROCESAR DATOS DE COMPRA (ARTICULO, PRECIO)
        # ################################################################
        articulo = datos_pedido_dict["articulo"]
        cantidad = datos_pedido_dict["cantidad"]
        cantidad_elementos = len(articulo)

        for elem in range(cantidad_elementos):
            print("Elemento: ", elem)
            print("articulo: ", articulo[elem])
            print("cantidad: ", cantidad[elem])
            print("-------------------")
        # ################################################################
        # REGEX, VARIABLE DE TESTEO Y INICIALIZACIÓN DE VARIABLE ENVIO
        # ################################################################
        results = []
        data = {}
        verificador = True
        verificador_m = True
        verificador_o = True
        patron = "^[A-Za-záéíóúÁÉÍÓÚÜü0-9]+(?i:[ _-][A-Za-záéíóúÁÉÍÓÚÜü]+)*$"
        patron2 = "^[0-9_-]+$"
        patron3 = "^[a-zA-Z0-9_-]+$"
        # ################################################################
        # TRABAJO EN LA VALIDACIÓN DE LOS DATOS DEL DICCIONARIO
        # GUARDAR DATOS DE FORMULARIO DE PERFIL
        # ################################################################
        id_nombre = datos_pedido_dict["id_nombre"]
        if not re.match(patron, id_nombre):
            verificador_m = False
            respuesta_id_nombre = "Debe ingresar un nombre valido"
            data["respuesta_id_nombre"] = respuesta_id_nombre
        else:
            data["respuesta_id_nombre"] = False

        id_apellido = datos_pedido_dict["id_apellido"]
        if not re.match(patron, id_apellido):
            verificador_m = False
            respuesta_id_apellido = "Debe ingresar un apellido valido"
            data["respuesta_id_apellido"] = respuesta_id_apellido
        else:
            data["respuesta_id_apellido"] = False

        id_provincia = datos_pedido_dict["id_provincia"]
        if id_provincia == "":
            verificador_m = False
            respuesta_id_provincia = "Debe ingresar una provincia valida"
            data["respuesta_id_provincia"] = respuesta_id_provincia
        else:
            data["respuesta_id_provincia"] = False

        id_cuil_cuit = datos_pedido_dict["id_cuil_cuit"]
        retorno_cuit = es_valido_cuit(id_cuil_cuit)

        if not retorno_cuit[0]:
            print(retorno_cuit[1])
            verificador_m = False
            respuesta_id_cuil_cuit = "Debe ingresar un cuil/cuit valido"
            data["respuesta_id_cuil_cuit"] = respuesta_id_cuil_cuit
        else:
            print(retorno_cuit[1])
            data["respuesta_id_cuil_cuit"] = False

        id_localidad = datos_pedido_dict["id_localidad"]
        if not re.match(patron, id_localidad):
            verificador_m = False
            respuesta_id_localidad = "Debe ingresar una localidad valida"
            data["respuesta_id_localidad"] = respuesta_id_localidad
        else:
            data["respuesta_id_localidad"] = False

        id_domicilio = datos_pedido_dict["id_domicilio"]
        if not re.match(patron, id_domicilio):
            verificador_m = False
            respuesta_id_domicilio = "Debe ingresar un domicilio valido"
            data["respuesta_id_domicilio"] = respuesta_id_domicilio
        else:
            data["respuesta_id_domicilio"] = False

        id_codigo_postal = datos_pedido_dict["id_codigo_postal"]
        if not re.match(patron3, id_codigo_postal):
            verificador_m = False
            respuesta_id_codigo_postal = "Debe ingresar un codigo postal valido"
            data["respuesta_id_codigo_postal"] = respuesta_id_codigo_postal
        else:
            data["respuesta_id_codigo_postal"] = False

        id_telefono_fijo = datos_pedido_dict["id_telefono_fijo"]
        if not re.match(patron2, id_telefono_fijo):
            verificador_m = False
            respuesta_id_telefono_fijo = "Debe ingresar un teléfono valido"
            data["respuesta_id_telefono_fijo"] = respuesta_id_telefono_fijo
        else:
            data["respuesta_id_telefono_fijo"] = False

        id_celular = datos_pedido_dict["id_celular"]
        if not re.match(patron2, id_celular):
            verificador_m = False
            respuesta_id_celular = "Debe ingresar un celular valido"
            data["respuesta_id_celular"] = respuesta_id_celular
        else:
            data["respuesta_id_celular"] = False

        id_provincia = datos_pedido_dict["id_provincia"]

        print(datos_pedido_dict["id_nombre"])
        print(datos_pedido_dict["id_apellido"])
        print(datos_pedido_dict["id_cuil_cuit"])
        print(datos_pedido_dict["id_documento"])
        print(datos_pedido_dict["id_localidad"])
        print(datos_pedido_dict["id_domicilio"])
        print(datos_pedido_dict["id_codigo_postal"])
        print(datos_pedido_dict["id_telefono_fijo"])
        print(datos_pedido_dict["id_celular"])
        id_documento = datos_pedido_dict["id_documento"]
        adonde = datos_pedido_dict["adonde"]
        data["respuesta_adonde"] = adonde


        # #############################################
        # CALCULO VALOR DE REFERENCIA
        # #############################################
        try:
            ref = Pedido.objects.last()
            referencia = ref.id + 10000
            print("1) referencia: ", referencia)
        except:
            referencia = 10000
            print("2) referencia: ", referencia)

        # #############################################
        # SI ENVIO A COMPRADOR
        # #############################################
        if adonde == "mantener":
            print("Mantener")
            print("chequeo en mantener", verificador_m)
            if verificador_m == True:
                print("Aquí va la lógica")
                data["verificador_m"] = True

                ver = Perfil.objects.get(usuario=request.user.pk)
                ver.nombre = id_nombre
                ver.apellido = id_apellido
                ver.provincia = id_provincia
                ver.localidad = id_localidad
                ver.domicilio = id_domicilio
                ver.codigo_postal = id_codigo_postal
                ver.telefono_fijo = id_telefono_fijo
                ver.celular = id_celular
                ver.cuil_cuit = id_cuil_cuit
                ver.documento = id_documento
                ver.save()

                # ########################################
                # Ver si ya no se cargo algo
                # ########################################
                try:
                    probar_pedido = Pedido.objects.get(
                        Q(usuario=request.user), Q(estado="A CONFIRMAR")
                    )
                    probar_pedido.delete()

                except:
                    print("no existe previo")

                grab_pm = Pedido(
                    usuario=request.user,
                    nombre=id_nombre,
                    apellido=id_apellido,
                    cuil_cuit=id_cuil_cuit,
                    domicilio=id_domicilio,
                    localidad=id_localidad,
                    provincia=id_provincia,
                    codigo_postal=id_codigo_postal,
                    telefono=id_celular,
                    documento=id_documento,
                    mensaje="---",
                    email=request.user.email,
                    referencia=referencia,
                )
                grab_pm.nombreextra = request.user.username
                grab_pm.articulo = articulo
                grab_pm.cantidad = cantidad
                grab_pm.referencia = referencia
                grab_pm.clave = clave

                grab_pm.save()
                data["referencia"] = referencia

        # #############################################
        # SI ENVIO A OTRO DESTINO
        # #############################################    
        if adonde == "otro":
            print("Otro")

            # ################################################################
            # Aquí se guardan los datos del formulario a otro para el envio
            # ################################################################
            id_envio_nombre = datos_pedido_dict["id_envio_nombre"]
            if not re.match(patron, id_envio_nombre):
                verificador_o = False
                respuesta_id_envio_nombre = "Debe ingresar un nombre valido"
                data["respuesta_id_envio_nombre"] = respuesta_id_envio_nombre
            else:
                data["respuesta_id_envio_nombre"] = False

            id_envio_apellido = datos_pedido_dict["id_envio_apellido"]
            if not re.match(patron, id_envio_apellido):
                verificador_o = False
                respuesta_id_envio_apellido = "Debe ingresar un apellido valido"
                data["respuesta_id_envio_apellido"] = respuesta_id_envio_apellido
            else:
                data["respuesta_id_envio_apellido"] = False

            id_envio_localidad = datos_pedido_dict["id_envio_localidad"]
            if not re.match(patron, id_envio_localidad):
                verificador_o = False
                respuesta_id_envio_localidad = (
                    "Debe ingresar una ciudad o localidad valida"
                )
                data["respuesta_id_envio_localidad"] = respuesta_id_envio_localidad
            else:
                data["respuesta_id_envio_localidad"] = False

            id_envio_documento = datos_pedido_dict["id_envio_documento"]
            if not re.match(patron2, id_envio_documento):
                verificador_o = False
                respuesta_id_envio_documento = "Debe ingresar un documento valido"
                data["respuesta_id_envio_documento"] = respuesta_id_envio_documento
            else:
                data["respuesta_id_envio_documento"] = False

            id_envio_domicilio = datos_pedido_dict["id_envio_domicilio"]
            if not re.match(patron, id_envio_domicilio):
                verificador_o = False
                respuesta_id_envio_domicilio = "Debe ingresar un domicilio valido"
                data["respuesta_id_envio_domicilio"] = respuesta_id_envio_domicilio
            else:
                data["respuesta_id_envio_domicilio"] = False

            id_envio_codigo_postal = datos_pedido_dict["id_envio_codigo_postal"]
            if not re.match(patron3, id_envio_codigo_postal):
                verificador_o = False
                respuesta_id_envio_codigo_postal = (
                    "Debe ingresar un codigo postal valido"
                )
                data[
                    "respuesta_id_envio_codigo_postal"
                ] = respuesta_id_envio_codigo_postal
            else:
                data["respuesta_id_envio_codigo_postal"] = False

            id_envio_telefono = datos_pedido_dict["id_envio_telefono"]
            if not re.match(patron2, id_envio_telefono):
                verificador_o = False
                respuesta_id_envio_telefono = "Debe ingresar un teléfono valido"
                data["respuesta_id_envio_telefono"] = respuesta_id_envio_telefono
            else:
                data["respuesta_id_envio_telefono"] = False

            id_envio_provincia = datos_pedido_dict["id_envio_provincia"]
            id_envio_mensaje = datos_pedido_dict["id_envio_mensaje"]

            if verificador_m == True and verificador_o == True:
                print("Aquí va la lógica")
                data["verificador_m"] = True
                data["verificador_o"] = True

                ver = Perfil.objects.get(usuario=request.user.pk)
                ver.nombre = id_nombre
                ver.apellido = id_apellido
                ver.provincia = id_provincia
                ver.localidad = id_localidad
                ver.domicilio = id_domicilio
                ver.codigo_postal = id_codigo_postal
                ver.telefono_fijo = id_telefono_fijo
                ver.celular = id_celular
                ver.cuil_cuit = id_cuil_cuit
                ver.save()

                # ########################################
                # Ver si ya no se cargo algo
                # ########################################
                try:
                    probar_pedido = Pedido.objects.get(
                        Q(usuario=request.user), Q(estado="A CONFIRMAR")
                    )
                    probar_pedido.delete()

                except:
                    print("no existe previo")

                grab_pm = Pedido(
                    usuario=request.user,
                    nombre=id_envio_nombre,
                    apellido=id_envio_apellido,
                    cuil_cuit=id_cuil_cuit,
                    domicilio=id_envio_domicilio,
                    localidad=id_envio_localidad,
                    provincia=id_envio_provincia,
                    codigo_postal=id_envio_codigo_postal,
                    telefono=id_envio_telefono,
                    documento=id_envio_documento,
                    mensaje=id_envio_mensaje,
                    email=request.user.email,
                    referencia=referencia,
                )
                grab_pm.nombreextra = request.user.username
                grab_pm.articulo = articulo
                grab_pm.cantidad = cantidad
                grab_pm.referencia = referencia
                grab_pm.clave = clave

                grab_pm.save()

                data["referencia"] = referencia

        print(verificador)
        # data["clave"] = clave
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)