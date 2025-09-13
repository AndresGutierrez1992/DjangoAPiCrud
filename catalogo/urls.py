from django.urls import path
from . import views


urlpatterns = [
    path('marcas/', views.lista_marcas, name='lista_marcas'),              # GET, POST
    path('marcas/<int:pk>/', views.detalle_marca, name='detalle_marca'),   # GET, PUT, PATCH, DELETE

    path('productos/', views.lista_productos, name='lista_productos'),              # GET, POST
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'), 

]


