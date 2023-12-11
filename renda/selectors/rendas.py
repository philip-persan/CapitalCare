from typing import Dict

from django.db.models import Avg, Max, Min, Sum
from django.db.models.functions import ExtractYear
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from ..models import Renda


def get_rendas_by_user(request) -> QuerySet[Renda]:
    rendas = Renda.objects.filter(
        owner=request.user
    ).select_related(
        'owner', 'tipo'
    )
    return rendas


def get_rendas_by_id(request, id: int) -> Renda:
    renda = get_object_or_404(Renda, id=id, owner=request.user)
    return renda


def get_aggregations_rendas(rendas: QuerySet[Renda]) -> Dict:
    values = rendas.aggregate(
        total=Sum('valor'),
        avg=Avg('valor'),
        min=Min('valor'),
        max=Max('valor')
    )
    return values


def get_annotations_rendas(rendas):

    rendas_por_tipo = rendas.values(
        'tipo__nome'
    ).annotate(
        total_por_tipo=Sum('valor')
    )

    return rendas_por_tipo


def get_aggregations_rendas_por_ano(rendas: QuerySet[Renda]) -> Dict:
    aggregations = rendas.annotate(
        ano=ExtractYear('data')
    ).values('ano').annotate(
        total=Sum('valor'),
        avg=Avg('valor'),
        min=Min('valor'),
        max=Max('valor')
    )
    return aggregations
