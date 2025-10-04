from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Endpoint para obtener token de autenticación
    Requiere: username y password
    Retorna: token de autenticación
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            'error': 'Se requieren username y password'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'error': 'Credenciales inválidas'
        }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Endpoint para registrar un nuevo usuario
    Requiere: username, password, email (opcional)
    Retorna: token de autenticación del usuario creado
    """
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')
    
    if not username or not password:
        return Response({
            'error': 'Se requieren username y password'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({
            'error': 'El usuario ya existe'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    
    token = Token.objects.create(user=user)
    
    return Response({
        'token': token.key,
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'message': 'Usuario creado exitosamente'
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logout(request):
    """
    Endpoint para cerrar sesión (eliminar token)
    Requiere autenticación
    """
    try:
        request.user.auth_token.delete()
        return Response({
            'message': 'Sesión cerrada exitosamente'
        }, status=status.HTTP_200_OK)
    except:
        return Response({
            'error': 'Error al cerrar sesión'
        }, status=status.HTTP_400_BAD_REQUEST)
