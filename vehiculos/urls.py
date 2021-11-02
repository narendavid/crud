from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrar-vehiculo/', views.registrarVehiculo),
    path('edicion-vehiculo/<cod>', views.edicionVehiculo),
    path('editar-vehiculo/', views.editarVehiculo),
    path('eliminar-vehiculo/<cod>', views.eliminarVehiculo)
]