from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from gasto.models import Gasto
from investimento.models import Investimento
from renda.models import Renda


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        rendas = Renda.objects.filter(
            owner=request.user
        ).select_related(
            'tipo'
        )
        total_rendas = rendas.aggregate(total=Sum('valor'))

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

        sem_lancamento = total_rendas.get('total') - total_gastos.get('total')

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
