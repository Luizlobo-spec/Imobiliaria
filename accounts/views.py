from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser


from django.contrib.auth import  login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomSerializer,LoginSerializer, LogoutSerializer
from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated



class SomenteAdmin(BasePermission):#Permite que só ADMIN façam list e create, em update e delete só o próprio usuário ou ADMIN
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return request.user.Usuario == 'ADMIN'
        return True

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email or request.user.Usuario == 'ADMIN' 
        
class LoginView(APIView):#view para login
    
    serializer_class = LoginSerializer

    def post (self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid()
        password = serializer.validated_data.get('password')
        email = serializer.validated_data.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user is not None:
            if user.password == password:
                login(request,user)
                return Response({"message":"Login realizado com sucesso!"}, status=status.HTTP_200_OK)
            return Response({'erro':    'senha incorreta'})
        return Response({"message":"Usuário ou senha inválidos."}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):#view para logout
    serializer_class = LogoutSerializer
    def post(self, request):
       logout(request)
       return Response({"message":"Logout realizado com sucesso!"}, status=status.HTTP_200_OK)
    

class ViewsetUser(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer
    permission_classes = [IsAuthenticated, SomenteAdmin]
    

