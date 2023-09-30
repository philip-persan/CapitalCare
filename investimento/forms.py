from typing import Any

from django import forms

from .models import Investimento, TipoInvestimento
from .selectors import get_tipo_investimento_by_user


class TipoInvestimentoForm(forms.ModelForm):
    class Meta:
        model = TipoInvestimento
        fields = ['nome', ]


class InvestimentoForm(forms.ModelForm):

    class Meta:
        model = Investimento
        fields = [
            'tipo', 'valor',
            'data', 'operacao',
            'ativo', 'obs'
        ]

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tipos_investimentos = get_tipo_investimento_by_user(request)
        self.fields['tipo'].queryset = tipos_investimentos

    def clean(self) -> dict[str, Any]:
        return super().clean()


class InvestimentoUpdateForm(forms.ModelForm):

    class Meta:
        model = Investimento
        fields = [
            'tipo', 'valor',
            'data', 'operacao',
            'ativo', 'obs'
        ]

    def clean(self) -> dict[str, Any]:
        return super().clean()
