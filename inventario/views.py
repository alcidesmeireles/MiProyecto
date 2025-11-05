from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Marca, Repuesto, Cliente
from .forms import MarcaForm, RepuestoForm, ClienteForm, BuscarRepuestoForm

def inicio(request):
    return render(request, "inventario/inicio.html")

def agregar_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = MarcaForm()
    return render(request, "inventario/form_marca.html", {"form": form})

def agregar_repuesto(request):
    if request.method == "POST":
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = RepuestoForm()
    return render(request, "inventario/form_repuesto.html", {"form": form})

def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ClienteForm()
    return render(request, "inventario/form_cliente.html", {"form": form})

def buscar_repuesto(request):
    resultados = []
    if request.method == "GET":
        form = BuscarRepuestoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            resultados = Repuesto.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarRepuestoForm()
    return render(request, "inventario/buscar.html", {"form": form, "resultados": resultados})
