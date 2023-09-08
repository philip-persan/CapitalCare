from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Categoria, Gasto, TipoGasto
from .serializers import (CategoriaSerializer, GastoSerializer,
                          TipoGastoSerializer)


class TipoGastoAPIView(ListAPIView):
    serializer_class = TipoGastoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TipoGasto.objects.filter(
            owner=self.request.user
        )


class CategoriaAPIView(ListAPIView):
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.filter(
            owner=self.request.user
        )


class GastoAPIView(ListAPIView):
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Gasto.objects.filter(
            owner=self.request.user
        ).select_related(
            'tipo', 'categoria'
        )
