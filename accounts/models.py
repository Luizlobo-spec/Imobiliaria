from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):#modelo customizado de usuário
    class role(models.TextChoices):
        
        CORRETOR = "CORRETOR"
        ADMIN = "ADMIN"
    Usuario = models.CharField(max_length=10, choices=role.choices, default=role.CORRETOR)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= []


