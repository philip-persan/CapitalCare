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
