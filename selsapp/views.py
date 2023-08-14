#from django.shortcuts import render, HttpResponse
#from rest_framework.generics import ListCreateAPIView
#from rest_framework.decorators import api_view
#from rest_framework import status   
#from django.http import JsonResponse
#import json as JSON

# rest_framework
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# models
from drf_yasg.utils import swagger_auto_schema
from .models import *
from django.db.models import *

# local
from .serializers import *
from .open_api_params import *

# function
from datetime import datetime

# Section 1 - 캘린더
## 모든 캘린더 불러오기
class GetCalendarAllView(APIView):    
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
    
## 캘린더 월별 불러오기
class GetCalendarMonthView(APIView):
    def get(self,request):
        now = datetime.now()
        querymonth = now.strftime('%Y-%m')
        events = Calendar.objects.filter(startDate__icontains = querymonth )
        serialized_event = CalendarAllDataSerializer(events, many=True)
        return Response(serialized_event.data)

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
            serialized_event = CalendarAllDataSerializer(event)
            return Response(serialized_event.data)
## 캘린더 일정 제거
class DeleteCalendarView(APIView):
    def delete(slef,request,eventId):
        is_exist = Calendar.objects.filter(eventId = eventId).exists()
        
        if is_exist:
            event = Calendar.objects.filter(eventId = eventId)
            event.delete()
            return Response('삭제 완료')
        else:
            return Response('해당하는 일정이 존재하지 않습니다!')
## 캘린더 일정 수정
class UpdateCalendarView(APIView):
    @swagger_auto_schema(manual_parameters=update_calendar_params)
    def patch(self,request):
        title = request.query_params.get('title')
        color = request.query_params.get('Color')
        event_id = request.query_params.get('eventId')
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')

        is_exists = Calendar.objects.filter(eventId = event_id).exists()

        if is_exists:
            event = Calendar.objects.filter(eventId = event_id)
            event.update(title=title)
            event.update(color=color)
            event.update(startDate = start_date)
            event.update(endDate = end_date)
            serialized_event = CalendarAllDataSerializer(event, many = True)
            return Response(serialized_event.data)
        else:
            return Response('존재하지 않는 일정입니다')

# Section 2 - 명부
# 전체 부원 불러오기
# function
## 0: 이름 오름차순, 1: 이름 내림차순, 2: 출석횟수 오름차순, 3: 출석횟수 내림차순, 4: 누적 봉사시간 오름차순, 5: 누적 봉사시간 내림차순, 6: 지각비 유무
class GetnameListView(APIView):
    permission_classes = []
    def get(self,request,function):
        if function == 0:
            namelist = Selslist.objects.order_by('name')
        elif function == 1:
            namelist = Selslist.objects.order_by('-name')
        elif function == 2:
            namelist = Selslist.objects.order_by('attendance','name')
        elif function == 3:
            namelist = Selslist.objects.order_by('-attendance','name')
        elif function == 4:
            namelist = Selslist.objects.order_by('accumulated_time','name')
        elif function == 5:
            namelist = Selslist.objects.order_by('-accumulated_time','name')
        elif function == 6:
            namelist = Selslist.objects.filter(latencyCost__gt = 0).order_by('name')
        serialized_selslist = NameSerializer(namelist,many = True)
        return Response(serialized_selslist.data)

## 부원 검색
class GetOneNameView(APIView):
    permission_classes = []
    def get(self,request,name):
        select_name = Selslist.objects.filter(name=name)
        serialized_name = NameSerializer(select_name, many=True)
        return Response(serialized_name.data)
    
## 부원 등록    
class PostNameListView(APIView):
    @swagger_auto_schema(manual_parameters=post_selslist_params)
    def post(self,request):
        school_id = request.query_params.get('school_id')
        sex = request.query_params.get('sex')
        department = request.query_params.get('department')
        name = request.query_params.get('name')
        is_admin = request.query_params.get('is_admin')
        attendance = request.query_params.get('attendance')
        accumulated_time = request.query_params.get('accumulated_time')
        accumulated_cost = request.query_params.get('accumulated_cost')
        latencyCost = request.query_params.get('latencyCost')
        
        add_name = Selslist(
               school_id = school_id,
               sex = sex,
               department = department,
               name = name,
               is_admin = is_admin,
               attendance = attendance,
               accumulated_time = accumulated_time,
               accumulated_cost = accumulated_cost,
               latencyCost = latencyCost,
            )
        add_name.save()
        serialized_name = NameSerializer(add_name)
        return Response(serialized_name.data)
    
        #return Response('success')
## 부원 수정
class UpdateNameListView(APIView):
    @swagger_auto_schema(manual_parameters=post_selslist_params)
    def patch(self,request):
        school_id = request.query_params.get('school_id')
        sex = request.query_params.get('sex')
        department = request.query_params.get('department')
        name = request.query_params.get('name')
        is_admin = request.query_params.get('is_admin')
        attendance = request.query_params.get('attendance')
        accumulated_time = request.query_params.get('accumulated_time')
        accumulated_cost = request.query_params.get('accumulated_cost')
        latencyCost = request.query_params.get('latencyCost')
        
        is_exist = Selslist.objects.filter(school_id = school_id).exists()

        if is_exist:
            user = Selslist.objects.filter(school_id = school_id)
            user.update(school_id = school_id)
            user.update(sex = sex)
            user.update(department = department)
            user.update(name = name)
            user.update(is_admin = is_admin)
            user.update(attendance = attendance)
            user.update(accumulated_time = accumulated_time)
            user.update(accumulated_cost = accumulated_cost)
            user.update(latencyCost = latencyCost)
            
            serialized_user = NameSerializer(user, many=True)
            return Response(serialized_user.data)
        else:
            return Response('존재하지 않는 부원입니다.')
## 전체 부원 삭제
class DeleteAllNameListView(APIView):
    def delete(self,request):
        data = Selslist.objects.all()
        data.delete()
        return Response('모든 데이터가 삭제됬습니다.')
    
class DeleteOneNameListView(APIView):
    def delete(self,request,school_id,name):
        data = Selslist.objects.filter(school_id = school_id, name=name)
        is_exist = data.exists()
        if is_exist:
            data.delete()
            return Response('선택 부원 정보가 삭제되었습니다.') 
        else:
            return Response('해당하는 부원이 없습니다.')

## 캘린더 일정에 명단 추가
class PostCalendarNameView(APIView):
    @swagger_auto_schema(manual_parameters=post_calendar_name_parmas)
    def post(self,request):
        event_id = request.query_params.get('eventId')
        name = request.query_params.get('name')
        school_id = request.query_params.get('school_id')
        is_exists = Calendar.objects.filter(eventId = event_id).exists()
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
            serialized_add_name = CalendarNameListSerializer(add_name)
            return Response(serialized_add_name.data)
        else:
            return Response('존재 하지 않는 일정입니다!')
class UpdateCalendarNameView(APIView):
    @swagger_auto_schema(manual_parameters=update_calendar_name_parmas)
    def patch(self,request):      
        event_id = request.query_params.get('eventId')
        name = request.query_params.get('name')
        school_id = request.query_params.get('school_id')
        state_point = request.query_params.get('state_point')
        state = request.query_params.get('state')
        attendanceTime = request.query_params.get('attendanceTime')

        is_exists = Calendar.objects.filter(eventId = event_id).exists()

        if is_exists:    
            user = Calendar_NameList.objects.filter(school_id = school_id, calendar_id = event_id)
            user_exists = user.exists()
            if user_exists:
                user.update(calendar_id = event_id)
                user.update(name = name)
                user.update(school_id = school_id)
                user.update(state_point = state_point)
                user.update(state = state)
                user.update(attendanceTime = attendanceTime)

                serialized_user = CalendarNameListSerializer(user, many=True)
                return Response(serialized_user.data)
            else:
                return Response('존재 하지 않는 인원입니다.')
        else: 
            return Response('존재 하지 않는 일정입니다.')
class DeleteCalendarNameOneView(APIView):
    def delete(self,request,eventId, school_id):
        user = Calendar_NameList.objects.filter(school_id = school_id, calendar_id = eventId)
        user_exists = user.exists()
        if user_exists:
            user.delete()
            return Response('삭제 완료')
        else:
            return Response('잘못된 명령입니다.')
class DeleteCalendarNameAllView(APIView):
    def delete(self,request,eventId):
        event = Calendar_NameList.objects.filter(calendar_id = eventId).all()
        event_exists = event.exists()
        if event_exists:
            event.delete()
            return Response('모든 데이터 삭제 완료')
        else:
            return Response('잘못된 명령입니다.')


    