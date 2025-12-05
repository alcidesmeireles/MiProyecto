from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Marca, Repuesto
from .forms import MarcaForm, RepuestoForm, ClienteForm, BuscarRepuestoForm

# vistas funcionales (ejemplo: inicio, buscar)
def inicio(request):
    return render(request, "inventario/inicio.html")

@login_required
def agregar_marca(request):   # ejemplo de decorador
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = MarcaForm()
    return render(request, "inventario/form_marca.html", {"form": form})

# Búsqueda con mensaje si no hay resultados
def buscar_repuesto(request):
    resultados = []
    mensaje = None
    if request.method == "GET":
        form = BuscarRepuestoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            if nombre:
                resultados = Repuesto.objects.filter(nombre__icontains=nombre)
                if not resultados:
                    mensaje = "No se encontraron repuestos con ese término."
            else:
                mensaje = "Ingresa un término de búsqueda."
    else:
        form = BuscarRepuestoForm()
    return render(request, "inventario/buscar.html", {"form": form, "resultados": resultados, "mensaje": mensaje})

# Agregar repuesto
def agregar_repuesto(request):
    if request.method == "POST":
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = RepuestoForm()
    return render(request, "inventario/form_repuesto.html", {"form": form})


# Acerca de: About
def about(request):
    texto = (
        "Este sitio Web ha sido creado por Alcides Meireles como parte del curso de Python en CoderHouse. "
        "Es la entrega final donde se ponen en práctica todos los conocimientos adquiridos."
    )
    return render(request, "inventario/about.html", {"texto": texto})

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class RepuestoListView(ListView):
    model = Repuesto
    template_name = "inventario/repuesto_list.html"
    context_object_name = "repuestos"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        qs = Repuesto.objects.all()
        if q:
            qs = qs.filter(nombre__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['repuestos'].exists():
            context['mensaje_empty'] = "No hay repuestos aún."
        return context

class RepuestoDetailView(DetailView):
    model = Repuesto
    template_name = "inventario/repuesto_detail.html"
    context_object_name = "repuesto"

class RepuestoCreateView(LoginRequiredMixin, CreateView):
    model = Repuesto
    form_class = RepuestoForm
    template_name = "inventario/repuesto_form.html"
    success_url = reverse_lazy('repuesto_list')

class RepuestoUpdateView(LoginRequiredMixin, UpdateView):
    model = Repuesto
    form_class = RepuestoForm
    template_name = "inventario/repuesto_form.html"
    success_url = reverse_lazy('repuesto_list')

class RepuestoDeleteView(LoginRequiredMixin, DeleteView):
    model = Repuesto
    template_name = "inventario/repuesto_confirm_delete.html"
    success_url = reverse_lazy('repuesto_list')
