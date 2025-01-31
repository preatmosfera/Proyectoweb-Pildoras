from django.db import models


# Create your models here.
class Servicio(models.Model):
    tipo=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.tipo
    
class Venta(models.Model):
    producto=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    servicios=models.ForeignKey(Servicio, on_delete=models.CASCADE)
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='venta'
        verbose_name_plural='ventas'

    def __str__(self):
        return self.producto
