from typing import Dict

from django.db.models import Avg, Max, Min, Sum
from django.db.models.query import QuerySet

from .models import Categoria, Gasto, TipoGasto


def get_tipos_by_user(request) -> QuerySet[TipoGasto]:
    tipos = TipoGasto.objects.filter(
        owner=request.user
    ).select_related(
        'owner'
    )
    return tipos


def get_categorias_by_user(request) -> QuerySet[Categoria]:
    categorias = Categoria.objects.filter(
        owner=request.user
    ).select_related(
        'owner'
    )
    return categorias


def get_gastos_by_user(request) -> QuerySet[Gasto]:
    gastos = Gasto.objects.filter(
        owner=request.user
    ).select_related(
        'owner', 'tipo', 'categoria'
    )
    return gastos


def get_aggregations_gastos(rendas: QuerySet[Gasto]) -> Dict:
    values = rendas.aggregate(
        total=Sum('valor'),
        avg=Avg('valor'),
        min=Min('valor'),
        max=Max('valor')
    )
    return values
