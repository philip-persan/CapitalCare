from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View

from ..forms import CategoriaForm, GastoCreateForm, TipoGastoForm
from ..selectors import (get_aggregations_gastos, get_annotations_gastos,
                         get_gastos_by_user)
from ..services import (categoria_gasto_create, gasto_create,
                        gasto_create_parcelado, tipo_gasto_create)


class GastoCreateView(View):
    def get(self, request):
        form_gastos = GastoCreateForm(request)
        form_tipo = TipoGastoForm()
        form_categoria = CategoriaForm()
        ctx = {
            'form_gastos': form_gastos,
            'form_tipo': form_tipo,
            'form_categoria': form_categoria,
        }
        return render(request, 'gasto/pages/create_gastos.html', ctx)

    def post(self, request):
        POST = request.POST
        form_gastos = GastoCreateForm(request, data=POST)
        form_tipo = TipoGastoForm(request.POST or None)
        form_categoria = CategoriaForm(request.POST or None)

        if form_gastos.is_valid():
            data = form_gastos.cleaned_data
            parcelado = data.get('parcelado')

            if parcelado == 'Sim':
                gasto_create_parcelado(form_data=data, request=request)
            else:
                gasto_create(form_data=data, request=request)

        if form_tipo.is_valid():
            data = form_tipo.cleaned_data
            tipo_gasto_create(data, request)
        else:
            messages.error(request, 'Erro ao criar Tipo de Gasto')

        if form_categoria.is_valid():
            data = form_tipo.cleaned_data
            categoria_gasto_create(data, request)
        else:
            messages.error(request, 'Erro ao criar Categoria de Gasto')

        return redirect('gastos:gasto_create')


class GastoListView(View):

    def get(self, request):
        gastos = get_gastos_by_user(request)
        paginator = Paginator(gastos, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        values = get_aggregations_gastos(gastos)
        annotations = get_annotations_gastos(request)

        ctx = {
            'page_obj': page_obj,
            'valores': values,
            'annotations': annotations
        }
        return render(request, 'gasto/pages/list_gastos.html', ctx)
