from django.db.models.query import QuerySet

from ..models import TipoRenda


def get_tipos_by_user(request) -> QuerySet[TipoRenda]:
    tipos = TipoRenda.objects.filter(
        owner=request.user
    ).select_related(
        'owner'
    )
    return tipos


def get_tipo_by_id(id) -> QuerySet[TipoRenda]:
    tipo = TipoRenda.objects.get(
        id=id
    )
    return tipo
