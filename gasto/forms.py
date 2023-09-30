from typing import Any

from django import forms

from .models import Categoria, Gasto, TipoGasto
from .selectors import get_categorias_by_user, get_tipos_by_user


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_categoria', ]


class TipoGastoForm(forms.ModelForm):
    class Meta:
        model = TipoGasto
        fields = ['nome_tipo', ]


class GastoUpdateForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = [
            'descricao', 'tipo',
            'categoria', 'valor',
            'data', 'obs'
        ]

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tipos_gastos = get_tipos_by_user(request)
        categorias_gastos = get_categorias_by_user(request)
        self.fields['tipo'].queryset = tipos_gastos
        self.fields['categoria'].queryset = categorias_gastos


class GastoCreateForm(forms.ModelForm):
    parcelado = forms.ChoiceField(
        choices=(
            ('Sim', 'Sim'), ('Não', 'Não')
        ),
        required=True,
        label='Gasto Parcelado'
    )
    n_vezes = forms.IntegerField(
        required=True,
        label='Quantidade de vezes',
        help_text='Em quantas vezes o valor foi parcelado'
    )

    class Meta:
        model = Gasto
        fields = [
            'descricao', 'tipo',
            'categoria', 'valor',
            'data', 'obs', 'parcelado',
            'n_vezes'
        ]
        labels = {
            'valor': 'Valor Total'
        }
        help_texts = {
            'descricao': 'Descrição do gasto. Ex.: Carnes Churrasco',
            'valor': 'Valor do Gasto ou Valor total do gasto se for parcelado'
            ' R$ 5.000 em 12 vezes',
            'data': 'Data do pagamento',
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tipos_gastos = get_tipos_by_user(request)
        categorias_gastos = get_categorias_by_user(request)
        self.fields['tipo'].queryset = tipos_gastos
        self.fields['categoria'].queryset = categorias_gastos

    def clean(self) -> dict[str, Any]:
        return super().clean()
