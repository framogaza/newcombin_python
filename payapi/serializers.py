from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Boleta

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ['codigoBarra','tipo','descripcion','fecha','importe','estado']

class BoletasImpagasFiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ['fecha','importe','codigoBarra']

class BoletasImpagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ['tipo','fecha','importe','codigoBarra']