from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email','telefone', 'escolaridade') 
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('telefone', 'escolaridade')}), 

    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone', 'escolaridade')}), 
    )

admin.site.register(usuario, UsuarioAdmin)
# Register your models here.
