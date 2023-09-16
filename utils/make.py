from random import randint, uniform

from django.core.exceptions import ObjectDoesNotExist
from faker import Faker

from gasto.models import Categoria, Gasto, TipoGasto
from investimento.models import Investimento, TipoInvestimento
from renda.models import Renda, TipoRenda
from users.models import User

fake = Faker('pt-BR')


class RendasFake:

    def __init__(self, username) -> None:
        self.user = username

    # ? cria salarios para todos os meses do ano informado
    def make_salarios_mes_ano(self, ano: int, valor: float, tipo_renda: str):
        user = User.objects.get(username=self.user)
        tipo_exist = TipoRenda.objects.filter(
            owner=user,
            nome=tipo_renda
        ).exists()

        if not tipo_exist:
            tipo = TipoRenda.objects.create(
                owner=user, nome=tipo_renda)
        else:
            tipo = TipoRenda.objects.get(owner=user, nome=tipo_renda)

        mes = 1
        try:
            for i in range(12):
                data = f'{ano}-{mes}-06'
                Renda.objects.create(
                    owner=user,
                    tipo=tipo,
                    valor=valor,
                    data=data
                )
                mes += 1
        except ObjectDoesNotExist:
            print(f'Tipo de Renda: "{tipo_renda}", não foi criado.')
            print(f'Crie o tipo de renda "{tipo_renda}", para continuar.')
            return f'Tipo de Renda: "{tipo_renda}", não foi criado.'

    def make_vendas_aleatorio(
        self,
        min_valor: int,
        max_valor: int,
        ano: int,
        tipo_vendas: str
    ):
        user = User.objects.get(username=self.user)
        tipo_exist = TipoRenda.objects.filter(
            owner=user,
            nome=tipo_vendas
        ).exists()

        if not tipo_exist:
            tipo = TipoRenda.objects.create(
                owner=user, nome=tipo_vendas)
        else:
            tipo = TipoRenda.objects.get(owner=user, nome=tipo_vendas)

        mes = 1
        try:
            for i in range(12):
                valor = uniform(a=min_valor, b=max_valor)
                data = f'{ano}-{mes}-{randint(1, 28)}'
                Renda.objects.create(
                    owner=user,
                    tipo=tipo,
                    valor=valor,
                    data=data
                )
                mes += 1
        except ObjectDoesNotExist:
            print('Tipo de Renda: "Vendas", não foi criado.')
            print('Crie o tipo de renda "Vendas", para continuar.')
            return 'Tipo de Renda: "Vendas", não foi criado.'


class InvestFake:

    def __init__(self, username) -> None:
        self.username = username

    def create_investimentos_por_mes(
        self,
        tipo_invest: str,
        min_valor: int,
        max_valor: int,
        ano: int,
        nome_ativo: str,
        tipo_operacao: str
    ):
        user = User.objects.get(username=self.username)

        tipo_exist = TipoInvestimento.objects.filter(
            owner=user,
            nome=tipo_invest
        ).exists()

        if not tipo_exist:
            tipo = TipoInvestimento.objects.create(
                owner=user, nome=tipo_invest)
        else:
            tipo = TipoInvestimento.objects.get(owner=user, nome=tipo_invest)

        mes = 1
        for i in range(12):
            valor = uniform(a=min_valor, b=max_valor)
            data = f'{ano}-{mes}-{randint(1, 28)}'
            Investimento.objects.create(
                owner=user,
                tipo=tipo,
                valor=valor,
                data=data,
                operacao=tipo_operacao,
                ativo=nome_ativo
            )
            mes += 1


class GastosFake:

    def __init__(self, username) -> None:
        self.username = username

    def create_conta_luz(self, min_valor: int, max_valor: int, ano: int):
        user = User.objects.get(username=self.username)
        tipo_exist = TipoGasto.objects.filter(
            owner=user,
            nome='Contas'
        ).exists()
        categoria_exist = Categoria.objects.filter(
            owner=user,
            nome='Conta de Luz'
        ).exists()

        if not tipo_exist:
            tipo = TipoGasto.objects.create(owner=user, nome='Contas')
        else:
            tipo = TipoGasto.objects.get(owner=user, nome='Contas')

        if not categoria_exist:
            categoria = Categoria.objects.create(
                owner=user, nome='Conta de Luz'
            )
        else:
            categoria = Categoria.objects.get(
                owner=user, nome='Conta de Luz'
            )

        mes = 1
        for i in range(12):
            valor = uniform(a=min_valor, b=max_valor)
            data = f'{ano}-{mes}-{randint(1, 28)}'
            Gasto.objects.create(
                owner=user,
                tipo=tipo,
                categoria=categoria,
                valor=valor,
                data=data
            )
            mes += 1

    def create_conta_agua(self, min_valor: int, max_valor: int, ano: int):
        user = User.objects.get(username=self.username)
        tipo_exist = TipoGasto.objects.filter(
            owner=user,
            nome='Contas'
        ).exists()
        categoria_exist = Categoria.objects.filter(
            owner=user,
            nome='Conta de Água'
        ).exists()

        if not tipo_exist:
            tipo = TipoGasto.objects.create(owner=user, nome='Contas')
        else:
            tipo = TipoGasto.objects.get(owner=user, nome='Contas')

        if not categoria_exist:
            categoria = Categoria.objects.create(
                owner=user, nome='Conta de Água'
            )
        else:
            categoria = Categoria.objects.get(
                owner=user, nome='Conta de Água'
            )

        mes = 1
        for i in range(12):
            valor = uniform(a=min_valor, b=max_valor)
            data = f'{ano}-{mes}-{randint(1, 28)}'
            Gasto.objects.create(
                owner=user,
                tipo=tipo,
                categoria=categoria,
                valor=valor,
                data=data
            )
            mes += 1

    def create_aluguel(self, aluguel: int, ano: int):
        user = User.objects.get(username=self.username)
        tipo_exist = TipoGasto.objects.filter(
            owner=user,
            nome='Contas'
        ).exists()
        categoria_exist = Categoria.objects.filter(
            owner=user,
            nome='Aluguel'
        ).exists()

        if not tipo_exist:
            tipo = TipoGasto.objects.create(owner=user, nome='Contas')
        else:
            tipo = TipoGasto.objects.get(owner=user, nome='Contas')

        if not categoria_exist:
            categoria = Categoria.objects.create(
                owner=user, nome='Aluguel'
            )
        else:
            categoria = Categoria.objects.get(
                owner=user, nome='Aluguel'
            )
        mes = 1
        for i in range(12):
            valor = aluguel
            data = f'{ano}-{mes}-{randint(1, 28)}'
            Gasto.objects.create(
                owner=user,
                tipo=tipo,
                categoria=categoria,
                valor=valor,
                data=data
            )
            mes += 1

    def create_any(
        self,
        tipo_nome: str,
        categoria_nome: str,
        min_valor: int,
        max_valor: int,
        ano: int,
        qtd: int,
        por_mes: bool,
    ):
        user = User.objects.get(username=self.username)
        tipo_exist = TipoGasto.objects.filter(
            owner=user,
            nome=tipo_nome
        ).exists()
        categoria_exist = Categoria.objects.filter(
            owner=user,
            nome=categoria_nome
        ).exists()

        if not tipo_exist:
            tipo = TipoGasto.objects.create(owner=user, nome=tipo_nome)
        else:
            tipo = TipoGasto.objects.get(owner=user, nome=tipo_nome)

        if not categoria_exist:
            categoria = Categoria.objects.create(
                owner=user, nome=categoria_nome
            )
        else:
            categoria = Categoria.objects.get(
                owner=user, nome=categoria_nome
            )

        if por_mes:
            mes = 1
            for i in range(12):
                valor = uniform(a=min_valor, b=max_valor)
                data = f'{ano}-{mes}-{randint(1, 28)}'
                Gasto.objects.create(
                    owner=user,
                    tipo=tipo,
                    categoria=categoria,
                    valor=valor,
                    data=data
                )
                mes += 1
        else:
            for i in range(qtd):
                valor = uniform(a=min_valor, b=max_valor)
                data = f'{ano}-{randint(1,12)}-{randint(1, 28)}'
                Gasto.objects.create(
                    owner=user,
                    tipo=tipo,
                    categoria=categoria,
                    valor=valor,
                    data=data
                )
        return f'Gasto: {tipo}/{categoria} criados'

    def delete_all_by_user(self):
        user = User.objects.get(username=self.username)
        tipos = TipoGasto.objects.filter(
            owner=user
        )
        categorias = Categoria.objects.filter(
            owner=user
        )
        contas = Gasto.objects.filter(
            owner=user
        )
        for i in range(len(contas)):
            contas[i].delete()
        for i in range(len(tipos)):
            tipos[i].delete()
        for i in range(len(categorias)):
            categorias[i].delete()

        return f'Gastos, tipos e categorias do usuário: {user}, apagados.'
