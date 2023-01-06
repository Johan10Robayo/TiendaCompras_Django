from django.contrib import admin
from .models import Cartegoria_prod,producto

# Register your models here.

class Categoria_prod_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class Producto_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Cartegoria_prod,Categoria_prod_admin)
admin.site.register(producto,Producto_admin)