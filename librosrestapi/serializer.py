from .models import LibrosRestApi
from rest_framework import serializers

"""
El primero me permite crear una clase para transportar los objetos a través de la red
"""
class LibrosRestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrosRestApi
        fields = '__all__'
