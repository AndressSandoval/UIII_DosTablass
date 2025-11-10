from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_videojuegos, name='inicio'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver_clientes/', views.ver_clientes, name='ver_clientes'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('borrar_cliente/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('ver_empleados/', views.ver_empleados, name='ver_empleados'),
    path('actualizar_empleado/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('borrar_empleado/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
]
