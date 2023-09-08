from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Investimento, TipoInvestimento
from .serializers import InvestimentoSerializer, TipoInvestSerializer


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
