from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *


class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = ['id', 'sarlavha', 'maqola']
    def validate_sarlavha(self, value):
        if len(value) < 10:
            raise ValidationError("Sarlavha kamida 10 ta harf bo'lsin!")
        return value 
   
class RasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasm
        fields = ['id', 'rasm', 'maqolaid']
    def validate_rasm(self, qiymat):
        if not qiymat.endswith('.jpg'):
            raise ValidationError("Rasm .jpg formatida bo'lishi shart!")
        return qiymat