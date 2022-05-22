from django.contrib import admin
from .models import Carro, Chassi

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', ) 

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('chassi', 'modelo', 'preco', )


# Register your models here.
