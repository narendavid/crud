from django.shortcuts import render, redirect
from .models import Vehiculo

# Create your views here.


def home(req):
    listaVehiculos = Vehiculo.objects.all()
    print(listaVehiculos)
    return render(req, "vehiculos.html", {"vehiculos": listaVehiculos})


def registrarVehiculo(req):
    codigo = req.POST['txtCodigo']
    tipo = req.POST['txtTipo']
    marca = req.POST['txtMarca']
    modelo = req.POST['txtModelo']
    version = req.POST['numVersion']
    placa = req.POST['txtPlaca']
    km = req.POST['numKm']

    Vehiculo.objects.create(
        codigo=codigo, tipo=tipo, marca=marca, modelo=modelo, version=version, placa=placa, kilometraje=km)
    return redirect('/')


def edicionVehiculo(req, cod):
    vehiculo = Vehiculo.objects.get(codigo=cod)
    return render(req, "editarVehiculos.html", {"vehiculo": vehiculo})


def editarVehiculo(req):
    codigo = req.POST['txtCodigo']
    tipo = req.POST['txtTipo']
    marca = req.POST['txtMarca']
    modelo = req.POST['txtModelo']
    version = req.POST['numVersion']
    placa = req.POST['txtPlaca']
    km = req.POST['numKm']
    vehiculo = Vehiculo.objects.get(codigo=codigo)
    vehiculo.tipo = tipo
    vehiculo.marca = marca
    vehiculo.modelo = modelo
    vehiculo.version = version
    vehiculo.placa = placa
    vehiculo.kilometraje = km
    vehiculo.save()
    return redirect('/')

def eliminarVehiculo(req, cod):
    vehiculo = Vehiculo.objects.get(codigo = cod)
    vehiculo.delete()
    return redirect('/')