from rest_framework.serializers import ModelSerializer
from .models import Selslist,Calendar
from rest_framework import serializers

class ListDataSerializer(ModelSerializer):
    class Meta:
        model = Selslist
        fields = '__all__'

class CalendarAllDataSerializer(ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'
        