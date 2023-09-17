import django_filters as df

from .models import Renda


class RendasFilter(df.FilterSet):
    tipo = df.CharFilter(
        field_name='tipo',
        lookup_expr='nome__icontains',
        label='Tipo',
    )
    mes = df.DateFilter(
        field_name='data',
        lookup_expr='month',
        label='Mês'
    )
    ano = df.DateFilter(
        field_name='data',
        lookup_expr='year',
        label='Ano'
    )
    data_maior = df.DateFilter(
        field_name='data',
        lookup_expr='gte',
        label='Data maior que'
    )
    data_menor = df.DateFilter(
        field_name='data',
        lookup_expr='lte',
        label='Data menor que'
    )
    valor_maior = df.NumberFilter(
        field_name='valor',
        lookup_expr='gte',
        label='Valor maior que'
    )
    valor_menor = df.NumberFilter(
        field_name='valor',
        lookup_expr='lte',
        label='Valor manor que'
    )

    class Meta:
        model = Renda
        fields = [
            'tipo', 'mes', 'ano', 'data_maior', 'data_menor',
            'valor_maior', 'valor_menor'
        ]
