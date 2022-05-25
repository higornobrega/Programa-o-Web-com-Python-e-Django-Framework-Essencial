from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustonUsuarioCreateForm, CustonUsuarioChangeForm
from .models import CustonUsuario

@admin.register(CustonUsuario)
class CustonUsuarioAdmin(UserAdmin):
    add_form = CustonUsuarioCreateForm
    form = CustonUsuarioChangeForm
    model = CustonUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )