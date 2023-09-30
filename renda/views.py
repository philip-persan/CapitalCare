from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from renda.selectors.rendas import (get_aggregations_rendas, get_rendas_by_id,
                                    get_rendas_by_user)

from .filters import RendasFilter
from .forms import RendaForm, TipoRendaForm
from .models import Renda, TipoRenda
from .serializers import RendaSerializer, TipoRendaSerializer
from .services import rendas_create, rendas_delete, rendas_update


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

        paginator = Paginator(rendas, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        valores = get_aggregations_rendas(rendas)

        ctx = {
            'page_obj': page_obj,
            'valores': valores,
            'filters': filter
        }
        return render(request, 'renda/pages/list_rendas.html', ctx)


class RendasCreateView(View):

    def get(self, request):
        form_renda = RendaForm(request)
        form_tipo_renda = TipoRendaForm()
        ctx = {
            'form_renda': form_renda,
            'form_tipo_renda': form_tipo_renda,
        }
        return render(request, 'renda/pages/create_rendas.html', ctx)

    def post(self, request):
        rendas_create(request)
        return redirect('rendas:rendas_create')


class RendasDeleteView(View):
    def get(self, request, id):
        rendas_delete(request, id)
        return redirect('rendas:rendas_list')


class RendasUpdateView(View):
    def get(self, request, id):
        renda = get_rendas_by_id(request, id)
        form = RendaForm(instance=renda, request=request)
        ctx = {
            'renda': renda,
            'form': form
        }
        return render(request, 'renda/pages/update_rendas.html', ctx)

    def post(self, request, id):
        renda = get_rendas_by_id(request, id)
        rendas_update(request, renda)
        return redirect('rendas:rendas_list')
