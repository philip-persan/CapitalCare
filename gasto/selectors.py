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


def get_annotations_gastos(request):
    gastos = get_gastos_by_user(request)

    gastos_por_descriao = gastos.values(
        'descricao'
    ).annotate(
        total_por_descricao=Sum('valor')
    )

    gastos_por_tipo = gastos.values(
        'tipo__nome_tipo'
    ).annotate(
        total_por_tipo=Sum('valor')
    )

    gastos_por_categoria = gastos.values(
        'categoria__nome_categoria'
    ).annotate(
        total_por_categoria=Sum('valor')
    )

    annotations = {
        'por_descricao': gastos_por_descriao,
        'por_tipo': gastos_por_tipo,
        'por_categoria': gastos_por_categoria,
    }

    return annotations
