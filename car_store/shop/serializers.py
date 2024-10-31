from rest_framework import serializers
from .models import *


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ['marka_name']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_name']


class CarSerializer(serializers.ModelSerializer):
    marka = MarkaSerializer()
    model = ModelSerializer()
    year = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Car
        fields = ['title', 'description', 'marka', 'model', 'price', 'color', 'volume', 'year', 'type_change', 'image', 'video']
