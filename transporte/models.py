from django.db import models
from django.utils.html import format_html

class CorreoArgentino(models.Model):
    responsable_inscripto_domicilio = models.TextField(default="")
    responsable_inscripto_sucursal = models.TextField("Monotributista y Consumidor Final", default="", blank=False, null=True)
    url = models.CharField(max_length=128, default="https://www.correoargentino.com.ar/MiCorreo/public/faqs")

    def url_sitio(self):

        return format_html(
            '<a href="https://www.correoargentino.com.ar/MiCorreo/public/faqs" target="_blank" style="background-color:#f00; padding:10px; color: #fff;">Ir</a>',
            
            )
 

class PreciosRIDomicilio(models.Model):
    correo_argentino = models.ForeignKey(CorreoArgentino, blank=False, null=True, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=12, decimal_places=2)
    zona_1 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_2 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_3 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_4 = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Precios Responsable Inscripto a Domicilio"
        verbose_name_plural = "Precios Responsable Inscripto a Domicilio"


class PreciosRISucursal(models.Model):
    correo_argentino = models.ForeignKey(CorreoArgentino, blank=False, null=True, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=12, decimal_places=2)
    zona_1 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_2 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_3 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_4 = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Precios Responsable Inscripto a Sucursal"
        verbose_name_plural = "Precios Responsable Inscripto a Sucursal"

class PreciosMCFDomicilio(models.Model):
    correo_argentino = models.ForeignKey(CorreoArgentino, blank=False, null=True, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=12, decimal_places=2)
    zona_1 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_2 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_3 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_4 = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Precios Monotributista y Consumidor Final a Domicilio"
        verbose_name_plural = "Precios Monotributista y Consumidor Final a Domicilio"

class PreciosMCFSucursal(models.Model):
    correo_argentino = models.ForeignKey(CorreoArgentino, blank=False, null=True, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=12, decimal_places=2)
    zona_1 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_2 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_3 = models.DecimalField(max_digits=12, decimal_places=2)
    zona_4 = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Precios Monotributista y Consumidor Final a Sucursal"
        verbose_name_plural = "Precios Monotributista y Consumidor Final a Sucursal"