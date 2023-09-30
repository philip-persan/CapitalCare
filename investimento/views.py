from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .forms import InvestimentoForm, InvestimentoUpdateForm
from .models import Investimento, TipoInvestimento
from .selectors import (get_aggregations_investimentos,
                        get_annotations_investimentos, get_investimento_by_id,
                        get_investimentos_by_user)
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
        form = InvestimentoForm(request, instance=investimento)

        ctx = {
            'investimento': investimento,
            'form': form
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
