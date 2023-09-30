from django.db import models

from users.models import User


class TipoGasto(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    nome_tipo = models.CharField(
        verbose_name='Nome',
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        default='Cartão de Crédito'
    )

    def __str__(self) -> str:
        return self.nome_tipo

    class Meta:
        verbose_name = 'Tipo de Gastos'
        verbose_name_plural = 'Tipos de Gastos'
        ordering = ['owner', 'nome_tipo']


class Categoria(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    nome_categoria = models.CharField(
        verbose_name='Nome',
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        default='Uber'
    )

    def __str__(self) -> str:
        return self.nome_categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['owner', 'nome_categoria']


class Gasto(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=50,
        blank=False,
        null=True
    )
    tipo = models.ForeignKey(
        TipoGasto,
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )
    categoria = models.ForeignKey(
        Categoria,
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
    obs = obs = models.CharField(
        verbose_name='Observações',
        max_length=255,
        blank=True,
        null=False,
        default='Sem Obervações'
    )

    def __str__(self) -> str:
        return f'{self.tipo} - {self.data.strftime("%d/%m/%Y")} - \
                {self.categoria}'

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-data', 'tipo', 'categoria']
