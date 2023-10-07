from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Categoria, Gasto, TipoGasto
from ..selectors import get_aggregations_gastos, get_annotations_gastos
from ..serializers import (CategoriaSerializer, GastosAggregationsSerializer,
                           GastoSerializer, GastosPorCategoriaSerializer,
                           GastosPorDescricaoSerializer,
                           GastosPorTipoSerializer, TipoGastoSerializer)


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


class GastoAggregationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gastos = Gasto.objects.filter(
            owner=request.user
        ).select_related(
            'tipo', 'categoria'
        )
        aggregations = get_aggregations_gastos(gastos)
        serializer = GastosAggregationsSerializer(aggregations)
        return Response(serializer.data)


class GastoAnnotationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        annotations = get_annotations_gastos(request)
        serializer = {
            'por_descricao': GastosPorDescricaoSerializer(
                annotations['por_descricao'],
                many=True
            ).data,
            'por_tipo': GastosPorTipoSerializer(
                annotations['por_tipo'],
                many=True
            ).data,
            'por_categoria': GastosPorCategoriaSerializer(
                annotations['por_categoria'],
                many=True
            ).data
        }
        return Response(serializer)
