from django.contrib import admin

from .models import Categoria, Gasto, TipoGasto


@admin.register(TipoGasto)
class TipoGastoAdmin(admin.ModelAdmin):
    list_display = 'owner', 'nome'
    list_display_links = 'owner', 'nome'
    list_filter = 'owner',


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'owner', 'nome'
    list_display_links = 'owner', 'nome'
    list_filter = 'owner',


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = 'owner', 'tipo', 'valor', 'data', 'categoria'
    list_display_links = 'owner', 'tipo', 'valor', 'data'
    list_filter = 'owner', 'tipo', 'categoria'
