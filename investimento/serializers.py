from rest_framework import serializers

from .models import Investimento, TipoInvestimento


class TipoInvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInvestimento
        fields = '__all__'


class InvestimentoSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField()
    valor = serializers.FloatField()
    data = serializers.DateField(format='%d/%m/%Y')

    class Meta:
        model = Investimento
        fields = '__all__'


class InvestimentoPorTipoSerializer(serializers.Serializer):
    tipo__nome = serializers.CharField(read_only=True)
    total_por_tipo = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)


class InvestimentoPorAtivoSerializer(serializers.Serializer):
    ativo = serializers.CharField(read_only=True)
    total_por_ativo = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)


class InvestimentoPorOperacaoSerializer(serializers.Serializer):
    operacao = serializers.CharField(read_only=True)
    total_por_operacao = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)


class InvestimentosAggregationsSerializer(serializers.Serializer):
    total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    avg = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    min = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    max = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
