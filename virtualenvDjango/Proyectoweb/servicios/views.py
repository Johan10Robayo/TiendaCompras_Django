from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.
def servicios(request):
    servicios=Servicio.objects.all()# importa todos los servicios construidos todas las tuplas

    return render(request,'servicios.html',{'servicios':servicios})