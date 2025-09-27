from rest_framework import serializers  # Importamos la clase base de serializers
from .models import Marca, Producto  # Importamos los modelos que vamos a serializar

# Serializer para la marca
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca            # Modelo asociado
        fields = ["id", "nombre", "pais"]  # Campos que vamos a devolver en JSON

# Serializer para crear/actualizar productos (acepta marca_id)
class ProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["id", "nombre", "precio", "marca"]

# Serializer para mostrar productos (muestra marca como string)
class ProductoSerializer(serializers.ModelSerializer):
    # Mostramos la categoría como nombre en lugar de solo el ID
    marca = serializers.StringRelatedField()

    class Meta:
        model = Producto
        fields = ["id", "nombre", "precio", "marca"]