from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from inventario.models import Marca  # usamos el modelo existente
from inventario.forms import MarcaForm  # usamos tu form ya hecho

class MarcaListView(ListView):
    model = Marca
    template_name = "marcas/marca_list.html"
    context_object_name = "marcas"


class MarcaCreateView(LoginRequiredMixin, CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = "marcas/marca_form.html"
    success_url = reverse_lazy("marca_list")


class MarcaUpdateView(LoginRequiredMixin, UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = "marcas/marca_form.html"
    success_url = reverse_lazy("marca_list")


class MarcaDeleteView(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = "marcas/marca_confirm_delete.html"
    success_url = reverse_lazy("marca_list")
