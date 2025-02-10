from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Venta
User= get_user_model()
# Create your models here.
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(total=models.Sum(models.F('cantidad') * models.F('producto_id__precio'), output_field=models.DecimalField(max_digits=10, decimal_places=2)))['total']

    class Meta:
        db_table = 'pedido'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class LineaPedido(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Venta, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.producto}"

    class Meta:
        db_table = 'linea_pedido'
        verbose_name = 'linea_pedido'
        verbose_name_plural = 'lineas_pedidos'
        ordering = ['id']

