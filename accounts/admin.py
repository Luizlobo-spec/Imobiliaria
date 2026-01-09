from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'Usuario', 'is_staff', 'is_active')
    list_filter = ('Usuario', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
# Register your models here.
