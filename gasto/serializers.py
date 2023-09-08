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
