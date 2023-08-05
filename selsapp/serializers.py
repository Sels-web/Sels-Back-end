from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class NameSerializer(ModelSerializer):
    class Meta:
        model = Selslist
        fields = '__all__'

class CalendarAllDataSerializer(ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'

class CalendarOneDataSerializer(ModelSerializer):
    class Meta:
        model = Calendar
        # fileds = ['title','startDate','endDate','color']
        exclude = ['eventId']

class CalendarNameListSerializer(ModelSerializer):
    class Meta:
        model = Calendar_NameList
        fields = '__all__'