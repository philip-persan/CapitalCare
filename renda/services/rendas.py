
from datetime import date as dt

from django.contrib import messages

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
