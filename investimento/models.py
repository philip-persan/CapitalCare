from django.db import models

from users.models import User


class TipoInvestimento(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        default='Ações'
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Investimento'
        verbose_name_plural = 'Tipos de Investimento'
        ordering = ['owner', 'nome']


class Investimento(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    tipo = models.ForeignKey(
        TipoInvestimento,
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )
    valor = models.DecimalField(
        verbose_name='Valor',
        max_digits=11,
        decimal_places=2,
        blank=False,
        null=True
    )
    data = models.DateField(
        verbose_name='Data',
        auto_created=False
    )
    operacao = models.CharField(
        verbose_name='Tipo de Operação',
        max_length=50,
        blank=False,
        null=False,
        choices=(
            ('Compra', 'Compra'),
            ('Venda', 'Venda')
        ),
        default='Compra'
    )
    ativo = models.CharField(
        verbose_name='Ativo',
        max_length=10,
        blank=False,
        null=True,
    )
    obs = models.CharField(
        verbose_name='Observações',
        max_length=255,
        blank=True,
        null=False,
        default='Sem Obervações'
    )

    def __str__(self) -> str:
        return f'{self.tipo} - {self.data.strftime("%d/%m/%Y")}'

    class Meta:
        verbose_name = 'Investimento'
        verbose_name_plural = 'Investimentos'
        ordering = ['owner', '-data', 'tipo']
