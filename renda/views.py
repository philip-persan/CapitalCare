from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from renda.selectors.rendas import get_aggregations_rendas, get_rendas_by_user

from .filters import RendasFilter
from .models import Renda, TipoRenda
from .serializers import RendaSerializer, TipoRendaSerializer


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


class RendasListView(View):

    def get(self, request):
        rendas = get_rendas_by_user(request)
        filter = RendasFilter(request.GET, queryset=rendas)
        rendas = filter.qs
        valores = get_aggregations_rendas(rendas)
        ctx = {
            'rendas': rendas,
            'valores': valores,
            'filters': filter
        }
        return render(request, 'renda/pages/list_rendas.html', ctx)
