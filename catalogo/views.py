from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Marca, Producto
from .serializers import MarcaSerializer, ProductoSerializer, ProductoCreateSerializer

# ViewSet para Marca
class MarcaViewSet(viewsets.ModelViewSet):
    """
    ViewSet que gestiona automáticamente:
    - Listar (GET /marcas/)
    - Detalle (GET /marcas/{id}/)
    - Crear (POST /marcas/)
    - Actualizar (PUT /marcas/{id}/)
    - Actualizar parcial (PATCH /marcas/{id}/)
    - Eliminar (DELETE /marcas/{id}/)
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

# ViewSet para Producto
class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet que gestiona automáticamente:
    - Listar (GET /productos/)
    - Detalle (GET /productos/{id}/)
    - Crear (POST /productos/)
    - Actualizar (PUT /productos/{id}/)
    - Actualizar parcial (PATCH /productos/{id}/)
    - Eliminar (DELETE /productos/{id}/)
    """
    queryset = Producto.objects.all()
    
    def get_serializer_class(self):
        """
        Usa diferentes serializers según la acción:
        - Para crear/actualizar: ProductoCreateSerializer
        - Para mostrar: ProductoSerializer
        """
        if self.action in ['create', 'update', 'partial_update']:
            return ProductoCreateSerializer
        return ProductoSerializer

    def create(self, request, *args, **kwargs):
        """Personaliza la creación para retornar con ProductoSerializer"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        producto = serializer.save()
        
        # Retornar con el serializer de lectura
        response_serializer = ProductoSerializer(producto)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Personaliza la actualización para retornar con ProductoSerializer"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        producto = serializer.save()

        # Retornar con el serializer de lectura
        response_serializer = ProductoSerializer(producto)
        return Response(response_serializer.data)