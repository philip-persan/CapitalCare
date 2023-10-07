from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Investimento, TipoInvestimento
from ..selectors import (get_aggregations_investimentos,
                         get_annotations_investimentos,
                         get_investimentos_by_user)
from ..serializers import (InvestimentoPorAtivoSerializer,
                           InvestimentoPorOperacaoSerializer,
                           InvestimentoPorTipoSerializer,
                           InvestimentosAggregationsSerializer,
                           InvestimentoSerializer, TipoInvestSerializer)


class TipoInvestimentosAPIView(ListAPIView):
    serializer_class = TipoInvestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TipoInvestimento.objects.filter(owner=self.request.user)


class InvestimentosAPIView(ListAPIView):
    serializer_class = InvestimentoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Investimento.objects.filter(
            owner=self.request.user
        ).select_related('tipo')


class InvestimentosAggregationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        investimentos = get_investimentos_by_user(request)
        agreggartions = get_aggregations_investimentos(investimentos)

        serializer = InvestimentosAggregationsSerializer(agreggartions)

        return Response(serializer.data)


class InvestimentosAnnotationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        annotations = get_annotations_investimentos(request)
        serializer = {
            'por_tipo': InvestimentoPorTipoSerializer(
                annotations['por_tipo'],
                many=True
            ).data,
            'por_ativo': InvestimentoPorAtivoSerializer(
                annotations['por_ativo'],
                many=True
            ).data,
            'por_operacao': InvestimentoPorOperacaoSerializer(
                annotations['por_operacao'],
                many=True
            ).data
        }
        return Response(serializer)
