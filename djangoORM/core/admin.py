from django.contrib import admin
from .models import Carro, Chassi, Montadora

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', ) 
@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome', ) 

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('chassi', 'modelo', 'preco', 'get_motoristas', )
    # Junta todos os motoristas com Python e retorna
    def get_motoristas(self, obj):
        return ', '.join([m.username for m in obj.motoristas.all()])

    # Muda o nome que vai ser mostrado no admin do Django
    get_motoristas.short_description = 'Motoristas' 
