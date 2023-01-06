from django.shortcuts import render,redirect
from .carro import Carro
from tienda.models import producto

# Create your views here.

def Agregar_producto(request,producto_id):
    carro=Carro(request)
    Producto=producto.objects.get(id=producto_id)
    carro.agregar(Producto)
    return redirect("Tienda")

def Eliminar_producto(request,producto_id):
    carro=Carro(request)
    Producto=producto.objects.get(id=producto_id)
    carro.eliminar(Producto)
    return redirect("Tienda")

def Restar_producto(request,producto_id):
    carro = Carro(request)
    Producto = producto.objects.get(id=producto_id)
    carro.restar_producto(Producto)
    return redirect("Tienda")

def Limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")