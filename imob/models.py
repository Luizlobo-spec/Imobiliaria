from django.db import models
from django.conf import settings

# Create your models here.
class Imovel(models.Model):
    class role(models.TextChoices):
        Disponivel = "DISPONIVEL"
        ALUGADO = "ALUGADO"
        inativo = "INATIVO"

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length= 500)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=15, choices=role.choices, default=role.inativo)
    corretor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True)
    created_at = models.DateTimeField(auto_now_add = True)

class Agendamento(models.Model):
    class role1(models.TextChoices):
        pendente = "PENDENTE"
        aprovado = "APROVADO"
        recusado = "RECUSADO"
        cancelado = "CANCELADO"
       
    imovel = models.ForeignKey(Imovel, related_name = 'agenda', on_delete=models.CASCADE)
    data_visita = models.DateTimeField()
    status = models.CharField(max_length=15, choices=role1.choices, default=role1.cancelado)
    created_at = models.DateTimeField(auto_now_add=True)
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True)

class Contrato(models.Model):
    class role3(models.TextChoices):
        ativo = "ATIVO"
        encerrado = "ENCERRADO"
        cancelado = "CANCELADO"
    imovel = models.OneToOneField(Imovel, related_name='contrato', on_delete=models.CASCADE)

    corretor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_mensal = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    status = models.CharField(max_length=15, choices=role3.choices, default=role3.cancelado)
    created_at = models.DateTimeField(auto_now_add=True)




    

