from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('agregar-marca/', views.agregar_marca, name="agregar_marca"),
    path('agregar-repuesto/', views.agregar_repuesto, name="agregar_repuesto"),
    path('agregar-cliente/', views.agregar_cliente, name="agregar_cliente"),
    path('buscar-repuesto/', views.buscar_repuesto, name="buscar_repuesto"),
]
