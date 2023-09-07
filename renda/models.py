from django.db import models

from users.models import User


class TipoRenda(models.Model):
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
        default='Salário'
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Renda'
        verbose_name_plural = 'Tipos de Renda'
        ordering = ['owner', 'nome']


class Renda(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    tipo = models.ForeignKey(
        TipoRenda,
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

    def __str__(self) -> str:
        return f'{self.tipo} - {self.data.strftime("%d/%m/%Y")}'
