from typing import Dict

from django.db.models import Avg, Max, Min, Sum
from django.db.models.query import QuerySet

from ..models import Renda


def get_rendas_by_user(request) -> QuerySet[Renda]:
    rendas = Renda.objects.filter(
        owner=request.user
    ).select_related(
        'owner', 'tipo'
    )
    return rendas


def get_aggregations_rendas(rendas: QuerySet[Renda]) -> Dict:
    values = rendas.aggregate(
        total=Sum('valor'),
        avg=Avg('valor'),
        min=Min('valor'),
        max=Max('valor')
    )
    return values
