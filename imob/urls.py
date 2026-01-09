from django.urls import path
from .views import ImovelView, AgendamentoView, ContratoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(ImovelView,AgendamentoView,ContratoView)

router.register(r'imovel',ImovelView, basename='Imovel')
router.register(r'agendamento',AgendamentoView, basename='Agendamento')
router.register(r'contrato',ContratoView, basename='Contrato')


urlpatterns = [
    *router.urls
]