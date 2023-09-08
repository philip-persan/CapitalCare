from random import randint

from faker import Faker

from renda.models import Renda, TipoRenda
from users.models import User

fake = Faker('pt-BR')


class DadosFake:

    def __init__(self, object, username) -> None:
        self.object = object
        self.user = username

    # ? cria salarios para todos os meses do ano
    def make_salarios_mes_ano(self, ano: str, valor: float):
        salario = TipoRenda.objects.get(nome='Salário')
        user = User.objects.get(username=self.user)
        mes = 1
        for i in range(12):
            data = f'{ano}-{mes}-06'
            Renda.objects.create(
                owner=user,
                tipo=salario,
                valor=valor,
                data=data
            )
            mes += 1
