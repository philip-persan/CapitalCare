import django_filters as df

from .models import Renda


class RendasFilter(df.FilterSet):
    tipo = df.CharFilter(
        field_name='tipo',
        lookup_expr='nome__icontains',
        label='Tipo',
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
        label='Valor menor que'
    )

    class Meta:
        model = Renda
        fields = [
            'tipo', 'data_maior', 'data_menor',
            'valor_maior', 'valor_menor'
        ]
