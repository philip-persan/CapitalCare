from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from ..forms import TipoInvestimentoForm
from ..models import TipoInvestimento


class TipoInvestimentoCreateView(View):
    def post(self, request):
        form = TipoInvestimentoForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            messages.success(
                request,
                'Tipo de investimento criado!'
            )

        return redirect('investimentos:investimentos_create')


class TipoInvestimentoDeleteView(View):
    def get(self, request, id):
        tipo = get_object_or_404(TipoInvestimento, id=id)
        tipo.delete()
        messages.success(
            request,
            'Tipo de investimento apagado!'
        )
        return redirect('investimentos:investimentos_create')
