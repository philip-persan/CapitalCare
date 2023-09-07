import re

from django.core.exceptions import ValidationError


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'A Senha deve ser forte, contendo caracteres maísculos, minúsculos e números.'  # noqa
        ),
            code='invalid'
        )
