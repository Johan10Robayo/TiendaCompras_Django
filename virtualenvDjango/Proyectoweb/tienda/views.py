from django.shortcuts import render
from .models import producto
# Create your views here.

def tienda(request):
    productos=producto.objects.all()
    return render(request,'tienda.html',{'productos':productos})