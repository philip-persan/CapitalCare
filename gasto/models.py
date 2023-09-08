from django.db import models

from users.models import User


class TipoGasto(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        default='Cartão'
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Gastos'
        verbose_name_plural = 'Tipos de Gastos'
        ordering = ['owner', 'nome']


class Categoria(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        default='Cartão'
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['owner', 'nome']


class Gasto(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
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
        ordering = ['owner', 'tipo', 'categoria']