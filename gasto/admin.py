from django.contrib import admin

from .models import Categoria, Gasto, TipoGasto


@admin.register(TipoGasto)
class TipoGastoAdmin(admin.ModelAdmin):
    list_display = 'owner', 'nome_tipo'
    list_display_links = 'owner', 'nome_tipo'
    list_filter = 'owner',


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'owner', 'nome_categoria'
    list_display_links = 'owner', 'nome_categoria'
    list_filter = 'owner',


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = 'owner', 'descricao', 'tipo', 'valor', 'data', 'categoria'
    list_display_links = 'owner', 'descricao', 'tipo', 'valor', 'data'
    list_filter = 'owner', 'tipo', 'categoria'
