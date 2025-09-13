from django.db import models  # Importamos models de Django para crear tablas

# Modelo para las categorías de productos
class Marca(models.Model):
    nombre = models.CharField(max_length=100)  # Campo de texto, máximo 100 caracteres
    pais = models.CharField(max_length=100) # Texto largo opcional

    def __str__(self):
        # Representación legible de la categoría en el admin
        return self.nombre

# Modelo para los productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)             # Nombre del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Precio con decimales
    marca = models.ForeignKey(
        Marca,                                         # Relación: cada producto pertenece a una categoría
        on_delete=models.CASCADE,                          # Si se borra la categoría, se borran sus productos
        related_name="productos"                           # Permite acceder a productos desde la categoría
    )

    def __str__(self):
        # Representación legible del producto en el admin
        return f"{self.nombre} - {self.precio}"