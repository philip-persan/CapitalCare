import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name='id',
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Phone',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
