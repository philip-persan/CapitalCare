from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Renda, TipoRenda
from ..selectors import (get_aggregations_rendas, get_annotations_rendas,
                         get_rendas_by_user)
from ..serializers import (RendasAggregationsSerializer, RendaSerializer,
                           RendasPorTipoSerializer, TipoRendaSerializer)


class TipoRendasAPIView(ListAPIView):
    serializer_class = TipoRendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TipoRenda.objects.filter(owner=self.request.user)


class RendasAPIView(ListAPIView):
    serializer_class = RendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Renda.objects.filter(
            owner=self.request.user
        ).select_related('tipo')


class RendasAgreggationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rendas = get_rendas_by_user(request)
        agreggations = get_aggregations_rendas(rendas)
        serializer = RendasAggregationsSerializer(agreggations)

        return Response(serializer.data)


class RendasAnnotationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        annotations = get_annotations_rendas(request)
        serializer = RendasPorTipoSerializer(annotations, many=True)

        return Response(serializer.data)
