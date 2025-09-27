from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crear el router
router = DefaultRouter()
router.register(r'marcas', views.MarcaViewSet)
router.register(r'productos', views.ProductoViewSet)

# Las URLs se generan automáticamente
urlpatterns = [
    path('', include(router.urls)),
]


