from typing import Dict

from django.db.models import Avg, Max, Min, Sum
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from .models import Investimento, TipoInvestimento


def get_tipo_investimento_by_user(request) -> QuerySet[TipoInvestimento]:
    tipos = TipoInvestimento.objects.filter(
        owner=request.user
    ).select_related(
        'owner'
    )
    return tipos


def get_investimentos_by_user(request) -> QuerySet[Investimento]:
    investimentos = Investimento.objects.filter(
        owner=request.user
    ).select_related(
        'owner', 'tipo'
    )
    return investimentos


def get_investimento_by_id(id):
    investimento = get_object_or_404(Investimento, id=id)
    return investimento


def get_aggregations_investimentos(investimentos: QuerySet[Investimento]) -> Dict:  # noqa
    values = investimentos.aggregate(
        total=Sum('valor'),
        avg=Avg('valor'),
        min=Min('valor'),
        max=Max('valor')
    )
    return values


def get_annotations_investimentos(request):
    investimentos = get_investimentos_by_user(request)

    investimentos_por_tipo = investimentos.values(
        'tipo__nome'
    ).annotate(
        total_por_tipo=Sum('valor')
    )

    investimentos_por_ativo = investimentos.values(
        'ativo'
    ).annotate(
        total_por_ativo=Sum('valor')
    )

    investimentos_por_operacao = investimentos.values(
        'operacao'
    ).annotate(
        total_por_operacao=Sum('valor')
    )

    annotations = {
        'por_tipo': investimentos_por_tipo,
        'por_ativo': investimentos_por_ativo,
        'por_operacao': investimentos_por_operacao
    }

    return annotations
