from rest_framework import serializers

from .models import Renda, TipoRenda


class TipoRendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRenda
        fields = 'owner', 'nome'


class RendaSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField()
    valor = serializers.FloatField()
    data = serializers.DateField(format='%d/%m/%Y')

    class Meta:
        model = Renda
        fields = [
            'owner', 'tipo', 'valor', 'data'
        ]
