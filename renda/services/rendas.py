
from datetime import date as dt

import pandas as pd
import plotly.graph_objs as go
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import ExtractMonth

from ..models import Renda, TipoRenda


def rendas_create(request) -> Renda:
    owner = request.user
    POST = request.POST
    tipo = POST['tipo']
    valor = POST['valor']
    date = POST['data'].split('/')
    date = dt(int(date[2]), int(date[1]), int(date[0]))
    obj = Renda.objects.create(
        owner=owner,
        tipo=TipoRenda.objects.get(owner=owner, id=tipo),
        valor=valor,
        data=date
    )
    msg = messages.success(request, f'Renda: {obj} criada com sucesso!')
    return msg


def rendas_delete(request, id):
    renda = Renda.objects.get(id=id)
    renda.delete()
    msg = messages.success(request, f'Renda: {renda} deletada com sucesso!')

    return msg


def rendas_update(request, renda):
    owner = request.user
    POST = request.POST
    tipo = TipoRenda.objects.get(owner=owner, id=POST['tipo'])
    valor = POST['valor']
    date = POST['data'].split('/')
    date = dt(int(date[2]), int(date[1]), int(date[0]))
    obj = renda
    obj.tipo = tipo
    obj.valor = valor
    obj.data = date
    obj.save()

    msg = messages.success(request, f'Renda: {obj} atualizado com sucesso!')
    return msg


def rendas_per_month_plotly_bar(queryset):
    data = queryset.annotate(
        month=ExtractMonth('data')
    ).values('month').annotate(
        total=Sum('valor')
    )

    df = pd.DataFrame.from_records(data)

    custom_colors = [
        '#d9ed92', '#b5e48c', '#99d98c', '#76c893', '#52b69a',
        '#34a0a4', '#aacc00', '#168aad', '#1e6091', '#184e77',
        '#0466c8', '#0353a4'
    ]

    fig = go.Figure(
        data=[
            go.Bar(
                x=df['month'], y=df['total'], marker_color=custom_colors,
            )
        ]
    )
    fig.update_layout(
        title='Rendas por Mês',
        xaxis_tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        xaxis_ticktext=[
            'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
            'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
        ],
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)'
    )

    chart = fig.to_html(full_html=False)

    return chart


def rendas_per_month_type_plotly_bar(queryset):
    data = queryset.annotate(
        month=ExtractMonth('data')
    ).values('month', 'tipo__nome').annotate(
        total=Sum('valor')
    )

    df = pd.DataFrame.from_records(data)

    custom_colors = {
        'Salário': '#0466c8',
        'Vendas': '#aacc00',
    }

    fig = go.Figure()

    for tipo, color in custom_colors.items():
        tipo_df = df[df['tipo__nome'] == tipo]
        fig.add_trace(
            go.Bar(
                x=tipo_df['month'],
                y=tipo_df['total'],
                name=tipo,
                marker_color=color
            )
        )

    fig.update_layout(
        title='Rendas por Mês & Tipo',
        xaxis_tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        xaxis_ticktext=[
            'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
            'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
        ],
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)'
    )

    chart = fig.to_html(full_html=False)

    return chart
