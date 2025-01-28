from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('servicio/<servicio_id>/', views.servicio, name="servicio"),
]