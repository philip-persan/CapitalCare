from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from gasto.models import Gasto
from gasto.selectors import (get_aggregations_gastos, get_annotations_gastos,
                             get_gastos_by_user)
from investimento.models import Investimento
from investimento.selectors import (get_aggregations_investimentos,
                                    get_investimentos_by_user)
from renda.models import Renda
from renda.selectors import get_aggregations_rendas, get_rendas_by_user


class DashboardView(LoginRequiredMixin, View):
    login_url = "home:login"

    def get(self, request):
        rendas = Renda.objects.filter(
            owner=request.user
        ).select_related(
            'tipo'
        )
        total_rendas = rendas.aggregate(total=Sum('valor'))
        # agreggations_per_year = get_aggregations_rendas_por_ano(rendas)

        investimentos = Investimento.objects.filter(
            owner=request.user
        ).select_related(
            'tipo'
        )
        total_investimentos = investimentos.aggregate(total=Sum('valor'))

        gastos = Gasto.objects.filter(
            owner=request.user
        ).select_related(
            'tipo', 'categoria'
        )
        total_gastos = gastos.aggregate(total=Sum('valor'))

        try:
            sem_lancamento = total_rendas.get(
                'total') - total_gastos.get('total') - total_investimentos.get('total')  # noqa
        except TypeError:
            sem_lancamento = total_rendas.get('total') - 0

        ctx = {
            'rendas': rendas,
            'total_rendas': total_rendas,
            'investimentos': investimentos,
            'total_investimentos': total_investimentos,
            'gastos': gastos,
            'total_gastos': total_gastos,
            'sem_lancamento': sem_lancamento
        }
        return render(request, 'dashboard/pages/dashboard.html', ctx)


class VisaoGeralView(LoginRequiredMixin, View):
    login_url = "home:login"

    def get(self, request):
        now = timezone.now()
        mes_atual = now.month
        ano_atual = now.year

        rendas_do_mes = get_rendas_by_user(request).filter(
            data__month=mes_atual, data__year=ano_atual
        )
        investimentos_do_mes = get_investimentos_by_user(request).filter(
            data__month=mes_atual, data__year=ano_atual
        )
        gastos_do_mes = get_gastos_by_user(request).filter(
            data__month=mes_atual, data__year=ano_atual
        )

        agr_rendas = get_aggregations_rendas(rendas_do_mes)
        agr_invest = get_aggregations_investimentos(investimentos_do_mes)
        agr_gastos = get_aggregations_gastos(gastos_do_mes)
        ann_gastos = get_annotations_gastos(gastos_do_mes)

        print(ann_gastos.get('por_descricao'))

        try:
            sem_lancamento = agr_rendas.get(
                'total') - agr_gastos.get('total') - agr_invest.get('total')  # noqa
        except TypeError:
            sem_lancamento = agr_rendas.get('total') - 0

        ctx = {
            'gastos_do_mes': gastos_do_mes,
            'total_rendas': agr_rendas,
            'total_investimentos': agr_invest,
            'total_gastos': agr_gastos,
            'sem_lancamento': sem_lancamento,
            'annotations_gastos': ann_gastos
        }

        return render(request, 'dashboard/pages/visao_geral.html', ctx)
