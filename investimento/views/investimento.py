from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from ..forms import (InvestimentoForm, InvestimentoUpdateForm,
                     TipoInvestimentoForm)
from ..models import Investimento, TipoInvestimento
from ..selectors import (get_aggregations_investimentos,
                         get_annotations_investimentos, get_investimento_by_id,
                         get_investimentos_by_user)


class InvestimentosListView(View):

    def get(self, request):
        investimentos = get_investimentos_by_user(request)
        annotations = get_annotations_investimentos(request)

        paginator = Paginator(investimentos, 15)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        valores = get_aggregations_investimentos(investimentos)

        ctx = {
            'page_obj': page_obj,
            'valores': valores,
            'annotations': annotations
        }
        return render(request, 'investimento/pages/list_investimentos.html', ctx)  # noqa


class InvestimentoUpdateView(View):

    def get(self, request, id):
        investimento = get_investimento_by_id(id)
        form_investimento = InvestimentoForm(request, instance=investimento)

        ctx = {
            'investimento': investimento,
            'form': form_investimento
        }

        return render(
            request,
            'investimento/pages/update_investimento.html',
            ctx
        )

    def post(self, request, id):
        investimento = get_investimento_by_id(id)
        form = InvestimentoUpdateForm(request.POST, instance=investimento)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Investimento {investimento} Alterado com Sucesso!'
            )
        else:
            messages.error(
                request, f'Erro ao salvar o Investimento {investimento}'
            )
        return redirect('investimentos:investimentos_list')


class InvestimentoCreateView(View):
    def get(self, request):
        form = InvestimentoForm(request)
        form_tipo = TipoInvestimentoForm()
        tipos = TipoInvestimento.objects.filter(
            owner=request.user
        )

        ctx = {
            'form': form,
            'form_tipo': form_tipo,
            'tipos': tipos
        }
        return render(request, 'investimento/pages/create_investimento.html', ctx)  # noqa

    def post(self, request):
        form = InvestimentoForm(request=request, data=request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()

            messages.success(
                request, 'Investimento Criado com Sucesso!'
            )
            return redirect('investimentos:investimentos_create')


class InvestimentoDeleteView(View):
    def get(self, request, id):
        investimento = get_object_or_404(Investimento, id=id)

        ctx = {
            'investimento': investimento
        }

        return render(request, 'investimento/pages/delete_investimento.html', ctx)  # noqa

    def post(self, request, id):
        invest = request.POST.get('id')
        investimento = get_object_or_404(Investimento, id=invest)

        messages.success(
            request, f'Investimento {investimento} apagado com sucesso!')

        investimento.delete()

        return redirect('investimentos:investimentos_list')
