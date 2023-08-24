from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from datetime import datetime
## return result
class NameSerializer(ModelSerializer):
    class Meta:
        model = Selslist
        exclude = ['id']

class CalendarAllDataSerializer(ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'
        
class CalendarOneDataSerializer(ModelSerializer):
    class Meta:
        model = Calendar
        # fileds = ['title','startDate','endDate','color']
        exclude = ['eventId','id']

class CalendarNameListSerializer(ModelSerializer):
    class Meta:
        model = Calendar_NameList
        fields = '__all__'

class ReferenceSerializer(ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'

## input 
class NameListSearchSerializer(serializers.Serializer):
    name = serializers.CharField(help_text = '이름 검색',required=False)
    school_id = serializers.CharField(help_text = '학번 검색', required=False)
    latencyCost = serializers.IntegerField(help_text='지각비',required=False,default=0)
    order      = serializers.CharField(help_text='정렬 순서:name, attendance, accumulated_time 사용 가능 내림차순: 앞에 - 붙이기', default='name')
    
class NameListRemoveSerializer(serializers.Serializer):
    range = serializers.CharField(help_text='삭제 범위: all, one', required=True)
    name = serializers.CharField(help_text = '삭제할 이름',required=False )
    school_id = serializers.CharField(help_text = '삭제할 학번',required=False )

class CalendarSearchSerializer(serializers.Serializer):
    range = serializers.CharField(help_text = '검색 범위:all, one, month', required=True)
    event_id = serializers.CharField(help_text = '특정 이벤트 검색', required=False)
    month = serializers.CharField(help_text = '월별 검색', required=False)

class AttendanceManageSerializer(serializers.Serializer):
    event_id = serializers.CharField(help_text = 'event id', required=True)
    current_time = serializers.DateTimeField(help_text = '요청 시간', default=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
    school_id = serializers.CharField(help_text = '학번', required= True)

class ReferenceSearchSerializer(serializers.Serializer):
    range = serializers.CharField(help_text = '검색 범위:all, one', required= True)
    id = serializers.IntegerField(help_text = '게시물 번호', required=False)

class ReferenceRemoveSerializer(serializers.Serializer):
    range = serializers.CharField(help_text='삭제 범위: all, one', required=True)
    id = serializers.IntegerField(help_text = '게시물 번호', required=False)
