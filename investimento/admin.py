from django.contrib import admin

from .models import Investimento, TipoInvestimento


@admin.register(TipoInvestimento)
class TipoInvestimentoAdmin(admin.ModelAdmin):
    list_display = 'owner', 'nome'
    list_display_links = 'owner', 'nome'
    list_filter = 'owner',


@admin.register(Investimento)
class InvestimentoAdmin(admin.ModelAdmin):
    list_display = 'owner', 'tipo', 'valor', 'data', 'operacao', 'ativo'
    list_display_links = 'owner', 'tipo', 'valor', 'data'
    list_filter = 'owner', 'tipo', 'operacao', 'ativo'
