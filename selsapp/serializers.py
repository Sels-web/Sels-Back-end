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

class NameListSearchSerializer(serializers.Serializer):
    order      = serializers.CharField(help_text='정렬 순서:name, attendance, accumulated_time 사용 가능', default='name')
    latencyCost = serializers.IntegerField(help_text='지각비', default=0)
    name = serializers.CharField(help_text = '이름 검색',required=False)