from django import forms
from .models import Marca, Repuesto, Cliente

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BuscarRepuestoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del repuesto", max_length=100)
