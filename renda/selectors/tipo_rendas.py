from django.db.models.query import QuerySet

from ..models import TipoRenda


def get_tipos_by_user(request) -> QuerySet[TipoRenda]:
    tipos = TipoRenda.objects.filter(
        owner=request.user
    ).select_related(
        'owner'
    )
    return tipos
