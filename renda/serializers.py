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


class RendasAggregationsSerializer(serializers.Serializer):
    total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    avg = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    min = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    max = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)


class RendasPorTipoSerializer(serializers.Serializer):
    tipo__nome = serializers.CharField(read_only=True)
    total_por_tipo = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
