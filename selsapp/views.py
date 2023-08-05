from django.shortcuts import render, HttpResponse

from rest_framework.decorators import api_view
from rest_framework import status   
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Selslist,Calendar,Calendar_NameList
from django.db.models import F,Sum, Count, Case, When
from django.http import JsonResponse
import json as JSON

from .serializers import *
from .open_api_params import *

class GetTestView(APIView):
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(manual_parameters=get_params)
    def get (self,request):
        return Response("Swagger Testing")
class PostTestView(APIView):    
    @swagger_auto_schema()
    def post(self,request):
        return Response("Swagger Schema")

# Section 1 - 캘린더
## 모든 캘린더 불러오기
class GetCalendarView(APIView):    
    permission_classes = [permissions.AllowAny]
    def get(self,request):
            calendar_events = Calendar.objects.all()
            serialized_calendar = CalendarAllDataSerializer(calendar_events, many=True)
            return Response(serialized_calendar.data)

## 캘린더 하나 불러오기
class GetCalendarOneView(APIView):
    def get(self,request,eventId):
        event = Calendar.objects.filter(eventId = eventId)
        serialized_event = CalendarOneDataSerializer(event, many=True)

        namelist = Calendar_NameList.objects.filter(calendar_id = eventId)
        serialized_namelist = CalendarNameListSerializer(namelist, many=True)

        combined_data = list(serialized_event.data)  # serialized_event 데이터를 리스트로 변환

        # serialized_namelist 데이터에서 필요한 필드만 추출하여 병합한 리스트에 추가
        for namelist_item in serialized_namelist.data:
            combined_data.append(namelist_item)
        return Response(combined_data)
## 캘린더 일정 등록
class PostCalendarView(APIView):
    @swagger_auto_schema(manual_parameters=post_calendar_params)
    def post(self,request):
        title = request.query_params.get('title')
        color = request.query_params.get('Color')
        event_id = request.query_params.get('eventId')
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')

        is_exist = Calendar.objects.filter(eventId = event_id).exists()

        if is_exist:
            return Response('이미 있는 일정입니다!')
        else:
            event = Calendar(
                title=title,
                color=color,
                eventId=event_id,
                startDate=start_date,
                endDate=end_date
            )
            event.save()

            return Response('success!')

## 캘린더 일정에 명단 추가
class PostCalendarNameView(APIView):
    @swagger_auto_schema(manual_parameters=post_calendar_name_parmas)
    def post(self,request):
        event_id = request.query_params.get('eventId')
        name = request.query_params.get('name')
        school_id = request.query_params.get('school_id')
        is_exists = Calendar.objects.filter(eventId = event_id)
        if is_exists:
            add_name = Calendar_NameList(
                calendar_id = event_id,
                school_id = school_id,
                name = name,
                state_point = 0,
                state = 'default',
                attendanceTime = '2023-01-27T16:30'
            )
            add_name.save()
            return Response('success!')
        else:
            return Response('존재 하지 않는 일정입니다!')

# Section 2 - 명부
# 전체 명단 불러오기
class GetnameListView(APIView):
    permission_classes = []
    def get(self,request):
        namelist = Selslist.objects.all()
        serialized_selslist = NameSerializer(namelist,many = True)
        return Response(serialized_selslist.data)

## 이름 검색
class GetOneNameView(APIView):
    def get(self,request,name):
        select_name = Selslist.objects.filter(name=name)
        serialized_name = NameSerializer(select_name, many=True)
        return Response(serialized_name.data)
    
