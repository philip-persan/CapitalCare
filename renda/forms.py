from django import forms

from .models import Renda, TipoRenda
from .selectors.tipo_rendas import get_tipos_by_user


class TipoRendaForm(forms.ModelForm):
    class Meta:
        model = TipoRenda
        fields = ['nome', ]


class RendaForm(forms.ModelForm):

    class Meta:
        model = Renda
        fields = ['tipo', 'valor', 'data']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tipos_renda = get_tipos_by_user(request)
        self.fields['tipo'].queryset = tipos_renda
