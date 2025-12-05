from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)              # char 1
    descripcion = models.CharField(max_length=200)         # char 2
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='repuestos/', null=True, blank=True)  # imagen
    fecha_ingreso = models.DateField(auto_now_add=False, null=True, blank=True) # fecha
    codigo = models.IntegerField(unique=True)              # integer unique

    def __str__(self):
        return f"{self.nombre} ({self.marca})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

