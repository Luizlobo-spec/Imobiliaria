from django import views
from django.shortcuts import render
from rest_framework import viewsets
from .models import Imovel, Agendamento, Contrato   
from .serializers import SerializerImovel, SerializerAgendamento, SerializerContrato    
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
#permissions que serao usadas nas views
class owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.corretor == request.user or request.user.Usuario == 'ADMIN'
class owner_agendamento(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        return obj.criador == request.user or request.user.Usuario == 'ADMIN'
class owner_contrato(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'destroy':
            return request.user.Usuario == 'ADMIN'
        elif view.action == 'retrieve':
            return True
        return obj.corretor == request.user or request.user.Usuario == 'ADMIN'

class ImovelView(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = SerializerImovel
    filterset_fields = ['titulo']
  #  permissions que serao usdas: os metodos get serão liberados para qualquer um.
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action =='list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [owner]

        return [permission() for permission in permission_classes]
   

    def perform_create(self,serializer):
        serializer.save(corretor=self.request.user)

class AgendamentoView(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = SerializerAgendamento
    permission_classes = [IsAuthenticated, owner_agendamento] 
    filterset_fields = ['imovel']
    def perform_create(self, serializer):
        serializer.save(criador = self.request.user)



class ContratoView(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = SerializerContrato
    filterset_fields = ['imovel']
   
    permission_classes = [IsAuthenticated, owner_contrato]#para deletar, só ADMIN. Para atualizar, só o corretor dono do contrato ou ADMIN. Para fazer o retrieve, não há restrição

    def perform_create(self,serializer):
        serializer.save(corretor=self.request.user)

