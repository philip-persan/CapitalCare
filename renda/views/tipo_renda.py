from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from ..selectors import get_tipo_by_id


class TipoRendasDeleteView(View):
    def get(self, request, id):
        tipo = get_tipo_by_id(id)
        tipo.delete()
        messages.success(request, 'Tipo de Renda Apagado com Sucesso!')
        return redirect('rendas:rendas_create')
