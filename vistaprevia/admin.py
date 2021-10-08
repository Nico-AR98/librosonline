from django.contrib import admin
from vistaprevia.models import Categoria
from vistaprevia.models import Producto

class ProductoAdmin(admin.ModelAdmin):
    fields =['categoria', 'fecha_publicacion', 'producto', 'imagen']

admin.site.register(Producto, ProductoAdmin)



admin.site.register(Categoria)
#admin.site.register(Producto)

