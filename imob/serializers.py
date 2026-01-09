from rest_framework import serializers
from .models import Imovel, Contrato, Agendamento

from imob.models import Agendamento


class SerializerAgendamento(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
        read_only_fields = ['criador']
class SerializerContrato(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'
        read_only_fields = ['corretor']
        
class SerializerImovel(serializers.ModelSerializer):
    contrato = SerializerContrato(read_only=True)
    agenda = SerializerAgendamento(many=True, read_only=True)
    class Meta:
        model = Imovel
        fields = '__all__'
        read_only_fields = ['corretor']
        
        
