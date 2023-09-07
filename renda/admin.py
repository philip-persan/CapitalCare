from django.contrib import admin

from .models import Renda, TipoRenda


@admin.register(TipoRenda)
class TipoRendaAdmin(admin.ModelAdmin):
    list_display = 'owner', 'nome'
    list_display_links = 'owner', 'nome'
    list_filter = 'owner',


@admin.register(Renda)
class RendaAdmin(admin.ModelAdmin):
    list_display = 'owner', 'tipo', 'valor', 'data'
    list_display_links = 'owner', 'tipo', 'valor', 'data'
    list_filter = 'owner', 'tipo'
