from rest_framework import serializers

from .models import Categoria, Gasto, TipoGasto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class TipoGastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGasto
        fields = '__all__'


class GastoSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField()
    categoria = serializers.StringRelatedField()
    valor = serializers.FloatField()
    data = serializers.DateField(format='%d/%m/%Y')

    class Meta:
        model = Gasto
        fields = '__all__'


class GastosPorDescricaoSerializer(serializers.Serializer):
    descricao = serializers.CharField(read_only=True)
    total_por_descricao = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)


class GastosPorTipoSerializer(serializers.Serializer):
    tipo__nome_tipo = serializers.CharField(read_only=True)
    total_por_tipo = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)


class GastosPorCategoriaSerializer(serializers.Serializer):
    categoria__nome_categoria = serializers.CharField(read_only=True)
    total_por_categoria = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)


class GastosAggregationsSerializer(serializers.Serializer):
    total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    avg = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    min = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    max = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
