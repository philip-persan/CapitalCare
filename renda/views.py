from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .filters import RendasFilter
from .forms import RendaForm, TipoRendaForm
from .models import Renda, TipoRenda
from .selectors import (get_aggregations_rendas, get_annotations_rendas,
                        get_rendas_by_id, get_rendas_by_user, get_tipo_by_id,
                        get_tipos_by_user)
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

        annotations = get_annotations_rendas(request)

        paginator = Paginator(rendas, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        valores = get_aggregations_rendas(rendas)

        ctx = {
            'page_obj': page_obj,
            'valores': valores,
            'filters': filter,
            'annotations': annotations
        }
        return render(request, 'renda/pages/list_rendas.html', ctx)


class RendasCreateView(View):

    def get(self, request):
        form_renda = RendaForm(request)
        form_tipo_renda = TipoRendaForm()
        tipos_renda = get_tipos_by_user(request)
        ctx = {
            'form_renda': form_renda,
            'form_tipo_renda': form_tipo_renda,
            'tipos_renda': tipos_renda
        }
        return render(request, 'renda/pages/create_rendas.html', ctx)

    def post(self, request):
        POST = request.POST
        model = POST.get('model')

        if model == 'create_renda':
            rendas_create(request)
        else:
            form = TipoRendaForm(POST or None)
            if form.is_valid():
                tipo_renda = form.save(commit=False)
                tipo_renda.owner = request.user
                tipo_renda.save()

        return redirect('rendas:rendas_create')


class TipoRendasDeleteView(View):
    def get(self, request, id):
        tipo = get_tipo_by_id(id)
        tipo.delete()
        messages.success(request, 'Tipo de Renda Apagado com Sucesso!')
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
