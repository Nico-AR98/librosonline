from django.contrib import admin
from transporte.models import PreciosRIDomicilio 
from transporte.models import PreciosRISucursal 
from transporte.models import PreciosMCFDomicilio 
from transporte.models import PreciosMCFSucursal
from transporte.models import CorreoArgentino

class PreciosRIDomicilioInline(admin.TabularInline):

    model = PreciosRIDomicilio
    #classes = ['collapse']
    extra = 0
    readonly_fields = [
        "peso",  
        "zona_1",  
        "zona_2", 
        "zona_3", 
        "zona_4",
    ]

    def has_delete_permission(self, request, obj=None):
        return False

class PreciosRISucursalInline(admin.TabularInline):

    model = PreciosRISucursal
    #classes = ['collapse']
    extra = 0
    readonly_fields = [
        "peso",  
        "zona_1",  
        "zona_2", 
        "zona_3", 
        "zona_4",
    ]

    def has_delete_permission(self, request, obj=None):
        return False

class PreciosMCFDomicilioInline(admin.TabularInline):

    model = PreciosMCFDomicilio
    #classes = ['collapse']
    extra = 0
    readonly_fields = [
        "peso",  
        "zona_1",  
        "zona_2", 
        "zona_3", 
        "zona_4",
    ]

    def has_delete_permission(self, request, obj=None):
        return False

class PreciosMCFSucursalInline(admin.TabularInline):

    model = PreciosMCFSucursal
    classes = ['collapse']
    extra = 0
    readonly_fields = [
        "peso",  
        "zona_1",  
        "zona_2", 
        "zona_3", 
        "zona_4",
    ]

    def has_delete_permission(self, request, obj=None):
        return False

class CorreoArgentinoadmin(admin.ModelAdmin):
    fieldsets = [
        (
            "RESPONSABLE INSCRIPTO A DOMICILIO",
            {
                "fields": [
                    "responsable_inscripto_domicilio",
                ]
            },
        ),
        (
            "MONOTRIBUTISTA Y CONSUMIDOR FINAL A DOMICILIO",
            {
                "fields": [
                    "responsable_inscripto_sucursal",
                ]
            },
        ),         
        (
            "URL DE SITIO WEB",
            {
                "fields": [
                    "url",
                ]
            },
        ),  
    ]
    list_display = [
  
        "responsable_inscripto_domicilio",
        "responsable_inscripto_sucursal",
        "url_sitio",
    ]
 
    #def has_add_permission(self, request, obj=None):
    #    return False

    def has_delete_permission(self, request, obj=None):
        return False

    #inlines = [PreciosRIDomicilioInline, PreciosRISucursalInline, PreciosMCFDomicilioInline, PreciosMCFSucursalInline]
    
    inlines = [PreciosRIDomicilioInline, PreciosMCFDomicilioInline]
    actions = ["crear_tablas"]

    def crear_tablas(self, request, queryset):
        #print(queryset)
        for que in queryset:
            # ####################################################
            # 1) CALCULO RESPONSABLE INSCRIPTO DOMICILIO
            # ####################################################
            print(que.responsable_inscripto_domicilio)
            var = que.responsable_inscripto_domicilio
            var2 = var.replace("PESO ", "")
            var3 = var2.replace(".", "")

            #var2 = var.replace(",", ".")
            #print(var3)
            var4 = var3.replace(",", ".")
            print(var4)
            #print("---"*22)
   
            lista = var4.split()

            #print(lista)


            #print("---"*22)

            lista2 = []
            for x in lista:
                if x != "$":
                    lista2.append(x)


            #print(lista2)

            try:
                PreciosRIDomicilio.objects.all().delete()
            except:
                print("No hay datos a borrar")

            obj1 = PreciosRIDomicilio()
            obj1.correo_argentino = queryset[0]
            obj1.peso = lista2[0]
            obj1.zona_1 = lista2[1]
            obj1.zona_2 = lista2[2]
            obj1.zona_3 = lista2[3]
            obj1.zona_4 = lista2[4]
            obj1.save()
            obj2 = PreciosRIDomicilio()
            obj2.correo_argentino = queryset[0]
            obj2.peso = lista2[5]
            obj2.zona_1 = lista2[6]
            obj2.zona_2 = lista2[7]
            obj2.zona_3 = lista2[8]
            obj2.zona_4 = lista2[9]
            obj2.save()
            obj3 = PreciosRIDomicilio()
            obj3.correo_argentino = queryset[0]
            obj3.peso = lista2[10]
            obj3.zona_1 = lista2[11]
            obj3.zona_2 = lista2[12]
            obj3.zona_3 = lista2[13]
            obj3.zona_4 = lista2[14]
            obj3.save()
            obj4 = PreciosRIDomicilio()
            obj4.correo_argentino = queryset[0]
            obj4.peso = lista2[15]
            obj4.zona_1 = lista2[16]
            obj4.zona_2 = lista2[17]
            obj4.zona_3 = lista2[18]
            obj4.zona_4 = lista2[19]
            obj4.save()
            obj5 = PreciosRIDomicilio()
            obj5.correo_argentino = queryset[0]
            obj5.peso = lista2[20]
            obj5.zona_1 = lista2[21]
            obj5.zona_2 = lista2[22]
            obj5.zona_3 = lista2[23]
            obj5.zona_4 = lista2[24]
            obj5.save()
            obj6 = PreciosRIDomicilio()
            obj6.correo_argentino = queryset[0]
            obj6.peso = lista2[25]
            obj6.zona_1 = lista2[26]
            obj6.zona_2 = lista2[27]
            obj6.zona_3 = lista2[28]
            obj6.zona_4 = lista2[29]
            obj6.save()
            obj7 = PreciosRIDomicilio()
            obj7.correo_argentino = queryset[0]
            obj7.peso = lista2[30]
            obj7.zona_1 = lista2[31]
            obj7.zona_2 = lista2[32]
            obj7.zona_3 = lista2[33]
            obj7.zona_4 = lista2[34]
            obj7.save()
            obj8 = PreciosRIDomicilio()
            obj8.correo_argentino = queryset[0]
            obj8.peso = lista2[35]
            obj8.zona_1 = lista2[36]
            obj8.zona_2 = lista2[37]
            obj8.zona_3 = lista2[38]
            obj8.zona_4 = lista2[39]
            obj8.save()
            obj9 = PreciosRIDomicilio()
            obj9.correo_argentino = queryset[0]
            obj9.peso = lista2[40]
            obj9.zona_1 = lista2[41]
            obj9.zona_2 = lista2[42]
            obj9.zona_3 = lista2[43]
            obj9.zona_4 = lista2[44]
            obj9.save()
            #print("!!!!!!!!!!!!!!!!!!!!")

            # ####################################################
            # 2) CALCULO RESPONSABLE INSCRIPTO SUCURSAL
            # ####################################################
            varb = que.responsable_inscripto_sucursal
            varb2 = varb.replace("PESO ", "")
            varb3 = varb2.replace(".", "")

            #var2 = var.replace(",", ".")
            #print(varb3)
            varb4 = varb3.replace(",", ".")
            #print(varb4)
            #print("---"*22)
   
            listab = varb4.split()

            #print(listab)


            #print("---"*22)

            listab2 = []
            for x in listab:
                if x != "$":
                    listab2.append(x)


            #print(listab2)

            try:
                PreciosRISucursal.objects.all().delete()
            except:
                print("No hay datos a borrar")

            objb1 = PreciosRISucursal()
            objb1.correo_argentino = queryset[0]
            objb1.peso = listab2[0]
            objb1.zona_1 = listab2[1]
            objb1.zona_2 = listab2[2]
            objb1.zona_3 = listab2[3]
            objb1.zona_4 = listab2[4]
            objb1.save()
            objb2 = PreciosRISucursal()
            objb2.correo_argentino = queryset[0]
            objb2.peso = listab2[5]
            objb2.zona_1 = listab2[6]
            objb2.zona_2 = listab2[7]
            objb2.zona_3 = listab2[8]
            objb2.zona_4 = listab2[9]
            objb2.save()
            objb3 = PreciosRISucursal()
            objb3.correo_argentino = queryset[0]
            objb3.peso = listab2[10]
            objb3.zona_1 = listab2[11]
            objb3.zona_2 = listab2[12]
            objb3.zona_3 = listab2[13]
            objb3.zona_4 = listab2[14]
            objb3.save()
            objb4 = PreciosRISucursal()
            objb4.correo_argentino = queryset[0]
            objb4.peso = listab2[15]
            objb4.zona_1 = listab2[16]
            objb4.zona_2 = listab2[17]
            objb4.zona_3 = listab2[18]
            objb4.zona_4 = listab2[19]
            objb4.save()
            objb5 = PreciosRISucursal()
            objb5.correo_argentino = queryset[0]
            objb5.peso = listab2[20]
            objb5.zona_1 = listab2[21]
            objb5.zona_2 = listab2[22]
            objb5.zona_3 = listab2[23]
            objb5.zona_4 = listab2[24]
            objb5.save()
            objb6 = PreciosRISucursal()
            objb6.correo_argentino = queryset[0]
            objb6.peso = listab2[25]
            objb6.zona_1 = listab2[26]
            objb6.zona_2 = listab2[27]
            objb6.zona_3 = listab2[28]
            objb6.zona_4 = listab2[29]
            objb6.save()
            objb7 = PreciosRISucursal()
            objb7.correo_argentino = queryset[0]
            objb7.peso = listab2[30]
            objb7.zona_1 = listab2[31]
            objb7.zona_2 = listab2[32]
            objb7.zona_3 = listab2[33]
            objb7.zona_4 = listab2[34]
            objb7.save()
            objb8 = PreciosRISucursal()
            objb8.correo_argentino = queryset[0]
            objb8.peso = listab2[35]
            objb8.zona_1 = listab2[36]
            objb8.zona_2 = listab2[37]
            objb8.zona_3 = listab2[38]
            objb8.zona_4 = listab2[39]
            objb8.save()
            objb9 = PreciosRISucursal()
            objb9.correo_argentino = queryset[0]
            objb9.peso = listab2[40]
            objb9.zona_1 = listab2[41]
            objb9.zona_2 = listab2[42]
            objb9.zona_3 = listab2[43]
            objb9.zona_4 = listab2[44]
            objb9.save()




            # ####################################################
            # 3) CALCULO MONOTRIBUTISTA Y CONSUMIDOR FINAL DOMICILIO
            # ####################################################
            print(que.responsable_inscripto_domicilio)
            var = que.responsable_inscripto_domicilio
            var2 = var.replace("PESO ", "")
            var3 = var2.replace(".", "")

            #var2 = var.replace(",", ".")
            #print(var3)
            var4 = var3.replace(",", ".")
            #print(var4)
            #print("---"*22)
   
            lista = var4.split()

            #print(lista)


            #print("---"*22)

            lista2 = []
            for x in lista:
                if x != "$":
                    lista2.append(x)


            #print(lista2)

            try:
                PreciosMCFDomicilio.objects.all().delete()
            except:
                print("No hay datos a borrar")

            obj1 = PreciosMCFDomicilio()
            obj1.correo_argentino = queryset[0]
            obj1.peso = lista2[0]
            obj1.zona_1 = float(lista2[1])*1.21
            obj1.zona_2 = float(lista2[2])*1.21
            obj1.zona_3 = float(lista2[3])*1.21
            obj1.zona_4 = float(lista2[4])*1.21
            obj1.save()
            obj2 = PreciosMCFDomicilio()
            obj2.correo_argentino = queryset[0]
            obj2.peso = lista2[5]
            obj2.zona_1 = float(lista2[6])*1.21
            obj2.zona_2 = float(lista2[7])*1.21
            obj2.zona_3 = float(lista2[8])*1.21
            obj2.zona_4 = float(lista2[9])*1.21
            obj2.save()
            obj3 = PreciosMCFDomicilio()
            obj3.correo_argentino = queryset[0]
            obj3.peso = lista2[10]
            obj3.zona_1 = float(lista2[11])*1.21
            obj3.zona_2 = float(lista2[12])*1.21
            obj3.zona_3 = float(lista2[13])*1.21
            obj3.zona_4 = float(lista2[14])*1.21
            obj3.save()
            obj4 = PreciosMCFDomicilio()
            obj4.correo_argentino = queryset[0]
            obj4.peso = lista2[15]
            obj4.zona_1 = float(lista2[16])*1.21
            obj4.zona_2 = float(lista2[17])*1.21
            obj4.zona_3 = float(lista2[18])*1.21
            obj4.zona_4 = float(lista2[19])*1.21
            obj4.save()
            obj5 = PreciosMCFDomicilio()
            obj5.correo_argentino = queryset[0]
            obj5.peso = lista2[20]
            obj5.zona_1 = float(lista2[21])*1.21
            obj5.zona_2 = float(lista2[22])*1.21
            obj5.zona_3 = float(lista2[23])*1.21
            obj5.zona_4 = float(lista2[24])*1.21
            obj5.save()
            obj6 = PreciosMCFDomicilio()
            obj6.correo_argentino = queryset[0]
            obj6.peso = lista2[25]
            obj6.zona_1 = float(lista2[26])*1.21
            obj6.zona_2 = float(lista2[27])*1.21
            obj6.zona_3 = float(lista2[28])*1.21
            obj6.zona_4 = float(lista2[29])*1.21
            obj6.save()
            obj7 = PreciosMCFDomicilio()
            obj7.correo_argentino = queryset[0]
            obj7.peso = lista2[30]
            obj7.zona_1 = float(lista2[31])*1.21
            obj7.zona_2 = float(lista2[32])*1.21
            obj7.zona_3 = float(lista2[33])*1.21
            obj7.zona_4 = float(lista2[34])*1.21
            obj7.save()
            obj8 = PreciosMCFDomicilio()
            obj8.correo_argentino = queryset[0]
            obj8.peso = lista2[35]
            obj8.zona_1 = float(lista2[36])*1.21
            obj8.zona_2 = float(lista2[37])*1.21
            obj8.zona_3 = float(lista2[38])*1.21
            obj8.zona_4 = float(lista2[39])*1.21
            obj8.save()
            obj9 = PreciosMCFDomicilio()
            obj9.correo_argentino = queryset[0]
            obj9.peso = lista2[40]
            obj9.zona_1 = float(lista2[41])*1.21
            obj9.zona_2 = float(lista2[42])*1.21
            obj9.zona_3 = float(lista2[43])*1.21
            obj9.zona_4 = float(lista2[44])*1.21
            obj9.save()




            # ####################################################
            # 4) CALCULO MONOTRIBUTISTA Y CONSUMIDOR FINAL SUCURSAL
            # ####################################################
            varb = que.responsable_inscripto_sucursal
            varb2 = varb.replace("PESO ", "")
            varb3 = varb2.replace(".", "")

            #var2 = var.replace(",", ".")
            #print(varb3)
            varb4 = varb3.replace(",", ".")
            #print(varb4)
            #print("---"*22)
   
            listab = varb4.split()

            #print(listab)


            #print("---"*22)

            listab2 = []
            for x in listab:
                if x != "$":
                    listab2.append(x)


            print(listab2)

            try:
                PreciosMCFSucursal.objects.all().delete()
            except:
                print("No hay datos a borrar")

            obj1 = PreciosMCFSucursal()
            obj1.correo_argentino = queryset[0]
            obj1.peso = listab2[0]
            obj1.zona_1 = float(listab2[1])*1.21
            obj1.zona_2 = float(listab2[2])*1.21
            obj1.zona_3 = float(listab2[3])*1.21
            obj1.zona_4 = float(listab2[4])*1.21
            obj1.save()
            obj2 = PreciosMCFSucursal()
            obj2.correo_argentino = queryset[0]
            obj2.peso = listab2[5]
            obj2.zona_1 = float(listab2[6])*1.21
            obj2.zona_2 = float(listab2[7])*1.21
            obj2.zona_3 = float(listab2[8])*1.21
            obj2.zona_4 = float(listab2[9])*1.21
            obj2.save()
            obj3 = PreciosMCFSucursal()
            obj3.correo_argentino = queryset[0]
            obj3.peso = listab2[10]
            obj3.zona_1 = float(listab2[11])*1.21
            obj3.zona_2 = float(listab2[12])*1.21
            obj3.zona_3 = float(listab2[13])*1.21
            obj3.zona_4 = float(listab2[14])*1.21
            obj3.save()
            obj4 = PreciosMCFSucursal()
            obj4.correo_argentino = queryset[0]
            obj4.peso = listab2[15]
            obj4.zona_1 = float(listab2[16])*1.21
            obj4.zona_2 = float(listab2[17])*1.21
            obj4.zona_3 = float(listab2[18])*1.21
            obj4.zona_4 = float(listab2[19])*1.21
            obj4.save()
            obj5 = PreciosMCFSucursal()
            obj5.correo_argentino = queryset[0]
            obj5.peso = listab2[20]
            obj5.zona_1 = float(listab2[21])*1.21
            obj5.zona_2 = float(listab2[22])*1.21
            obj5.zona_3 = float(listab2[23])*1.21
            obj5.zona_4 = float(listab2[24])*1.21
            obj5.save()
            obj6 = PreciosMCFSucursal()
            obj6.correo_argentino = queryset[0]
            obj6.peso = listab2[25]
            obj6.zona_1 = float(listab2[26])*1.21
            obj6.zona_2 = float(listab2[27])*1.21
            obj6.zona_3 = float(listab2[28])*1.21
            obj6.zona_4 = float(listab2[29])*1.21
            obj6.save()
            obj7 = PreciosMCFSucursal()
            obj7.correo_argentino = queryset[0]
            obj7.peso = listab2[30]
            obj7.zona_1 = float(listab2[31])*1.21
            obj7.zona_2 = float(listab2[32])*1.21
            obj7.zona_3 = float(listab2[33])*1.21
            obj7.zona_4 = float(listab2[34])*1.21
            obj7.save()
            obj8 = PreciosMCFSucursal()
            obj8.correo_argentino = queryset[0]
            obj8.peso = listab2[35]
            obj8.zona_1 = float(listab2[36])*1.21
            obj8.zona_2 = float(listab2[37])*1.21
            obj8.zona_3 = float(listab2[38])*1.21
            obj8.zona_4 = float(listab2[39])*1.21
            obj8.save()
            obj9 = PreciosMCFSucursal()
            obj9.correo_argentino = queryset[0]
            obj9.peso = listab2[40]
            obj9.zona_1 = float(listab2[41])*1.21
            obj9.zona_2 = float(listab2[42])*1.21
            obj9.zona_3 = float(listab2[43])*1.21
            obj9.zona_4 = float(listab2[44])*1.21
            obj9.save()          
            print("!!!!!!!!!!!!!!!!!!!!")


            print("!!!!!!!!!!!!!!!!!!!!")






            print("-----")
            #print(que.monotributista_y_consumidor_final)

    crear_tablas.short_description = "Crear Tablas"


admin.site.register(CorreoArgentino, CorreoArgentinoadmin)