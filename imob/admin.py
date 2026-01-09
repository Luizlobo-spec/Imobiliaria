from django.contrib import admin

from .models import Imovel, Agendamento, Contrato   
@admin.register(Imovel)
class AdminImovel(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'endereco', 'cidade', 'valor_aluguel', 'status', 'created_at')
@admin.register(Agendamento)
class AdminAgendamento(admin.ModelAdmin):
    list_display = ( 'imovel', 'data_visita', 'status', 'created_at')
@admin.register(Contrato)
class AdminContrato(admin.ModelAdmin):
    list_display = ( 'imovel',  'data_inicio', 'data_fim', 'valor_mensal', 'status', 'created_at')

