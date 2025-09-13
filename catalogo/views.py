from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Marca, Producto
from .serializers import MarcaSerializer, ProductoSerializer

# MARCAS

@api_view(["GET", "POST"])
def lista_marcas(request):
    if request.method == "GET":
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Crea la marca
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def detalle_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)

    if request.method == "GET":
        serializer = MarcaSerializer(marca)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        # Actualización completa: debes mandar todos los campos
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PATCH":
        # Actualización parcial
        serializer = MarcaSerializer(marca, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        marca.delete()
        return Response({"detail": "Marca eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)


# PRODUCTOS

@api_view(["GET", "POST"])
def lista_productos(request):
    if request.method == "GET":
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Crea el producto
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "GET":
        serializer = ProductoSerializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PATCH":
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        producto.delete()
        return Response({"detail": "Producto eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)