
from datetime import date, timedelta
from typing import Any

from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Categoria, Gasto, TipoGasto


def gasto_create_parcelado(form_data: dict, request: HttpRequest):
    descricao = form_data.get('descricao')
    tipo: QuerySet[TipoGasto] = form_data.get('tipo')
    categoria: QuerySet[Categoria] = form_data.get('categoria')
    valor: float | Any = form_data.get('valor')
    data_gasto: date | Any = form_data.get('data')
    obs = form_data.get('obs')
    n_vezes: int | Any = form_data.get('n_vezes')
    valor_parcela = valor / n_vezes

    for i in range(n_vezes):
        new_descricao = f'{descricao} - {i+1}/{n_vezes}'
        Gasto.objects.create(
            owner=request.user,
            descricao=new_descricao,
            tipo=TipoGasto(tipo.id),
            categoria=Categoria(categoria.id),
            valor=valor_parcela,
            data=data_gasto,
            obs=obs
        )
        data_gasto += timedelta(31)
    msg = messages.success(request, 'Gasto Parcelado Criado com Sucesso!')
    return msg


def gasto_create(form_data: dict, request: HttpRequest):
    descricao = form_data.get('descricao')
    tipo: QuerySet[TipoGasto] = form_data.get('tipo')
    categoria: QuerySet[Categoria] = form_data.get('categoria')
    valor = form_data.get('valor')
    data_gasto = form_data.get('data')
    obs = form_data.get('obs')
    Gasto.objects.create(
        owner=request.user,
        descricao=descricao,
        tipo=TipoGasto(tipo.id),
        categoria=Categoria(categoria.id),
        valor=valor,
        data=data_gasto,
        obs=obs
    )
    msg = messages.success(request, 'Gasto Criado com Sucesso!')
    return msg


def tipo_gasto_create(form_data: dict, request: HttpRequest):
    nome = form_data.get('nome_tipo')
    tipo_gasto_obj = TipoGasto.objects.create(
        owner=request.user,
        nome_tipo=nome
    )
    msg = messages.success(
        request, f'Tipo de Gasto: {tipo_gasto_obj} Criado com Sucesso!')
    return msg


def categoria_gasto_create(form_data: dict, request: HttpRequest):
    nome = form_data.get('nome_categoria')
    categoria_obj = Categoria.objects.create(
        owner=request.user,
        nome_categoria=nome
    )
    msg = messages.success(
        request, f'Categoria de Gasto: {categoria_obj} Criado com Sucesso!')
    return msg
