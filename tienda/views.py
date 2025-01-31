from django.shortcuts import render
from .models import Venta, Servicio
# Create your views here.

def tienda(request):
    ventas = Venta.objects.all()

    # Crear un conjunto único de servicios
    servicios = set()
    for x in ventas:
            servicios.add(x.servicios)

    return render(request, "tienda/tienda.html", {"ventas": ventas, "servicios": servicios})

def servicio(request, servicio_id):
    servicio=Servicio.objects.get(id=servicio_id)
    ventas=Venta.objects.filter(servicios=servicio)
    return render(request, "tienda/servicio.html", {'servicio': servicio, "ventas": ventas})