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
    @swagger_auto_schema(query_serializer=CalendarSearchSerializer)
    def get(self,request):
            range = request.query_params.get('range')
            event_id = request.query_params.get('event_id')
            month = request.query_params.get('month')

            if range == 'all':
                calendar_events = Calendar.objects.all()
                serialized_calendar = CalendarAllDataSerializer(calendar_events, many=True)
                return Response(serialized_calendar.data, status=200)
            elif range == 'one':
                event = Calendar.objects.filter(eventId = event_id)
                serialized_event = CalendarOneDataSerializer(event, many=True)

                namelist = Calendar_NameList.objects.filter(calendar_id = event_id)
                serialized_namelist = CalendarNameListSerializer(namelist, many=True)

                combined_data = list(serialized_event.data)  # serialized_event 데이터를 리스트로 변환

                # serialized_namelist 데이터에서 필요한 필드만 추출하여 병합한 리스트에 추가
                for namelist_item in serialized_namelist.data:
                    combined_data.append(namelist_item)
                if combined_data:
                    return Response(combined_data,status=200)
                else:
                    return Response({'message': 'eventId is not exists'}, status=404)
                
            elif range == 'month':
                now = datetime.now()
                querymonth = now.strftime('%Y-%m')
                print(querymonth)
                events = Calendar.objects.filter(startDate__icontains = querymonth )
                serialized_event = CalendarAllDataSerializer(events, many=True)
                return Response(serialized_event.data,status=200)
            

## 캘린더 하나 불러오기
# class GetCalendarOneView(APIView):
#     def get(self,request,eventId):
#         event = Calendar.objects.filter(eventId = eventId)
#         serialized_event = CalendarOneDataSerializer(event, many=True)

#         namelist = Calendar_NameList.objects.filter(calendar_id = eventId)
#         serialized_namelist = CalendarNameListSerializer(namelist, many=True)

#         combined_data = list(serialized_event.data)  # serialized_event 데이터를 리스트로 변환

#         # serialized_namelist 데이터에서 필요한 필드만 추출하여 병합한 리스트에 추가
#         for namelist_item in serialized_namelist.data:
#             combined_data.append(namelist_item)
#         if combined_data:
#             return Response(combined_data,status=200)
#         else:
#             return Response({'message': 'eventId is not exists'}, status=404)
    
# ## 캘린더 월별 불러오기
# class GetCalendarMonthView(APIView):
#     def get(self,request):
#         now = datetime.now()
#         querymonth = now.strftime('%Y-%m')
#         events = Calendar.objects.filter(startDate__icontains = querymonth )
#         serialized_event = CalendarAllDataSerializer(events, many=True)
#         return Response(serialized_event.data,status=200)

## 캘린더 일정 등록
class PostCalendarView(APIView):
    @swagger_auto_schema(request_body= post_calendar_params)
    def post(self,request):
            event = CalendarAllDataSerializer(data = request.data)
            if event.is_valid():
                event_id = event.validated_data.get('eventId')
                if Calendar.objects.filter(eventId=event_id).exists():
                    return Response({'message': 'eventId already exists'}, status=400)
                event.save()
                return Response(event.data,status=201)
            else:
                return Response(event.errors, status=400)

## 캘린더 일정 수정
class UpdateCalendarView(APIView):
    @swagger_auto_schema(request_body = update_calendar_params)
    def patch(self,request):
        title = request.data.get('title')
        color = request.data.get('Color')
        event_id = request.data.get('eventId')
        start_date = request.data.get('startDate')
        end_date = request.data.get('endDate')

        is_exists = Calendar.objects.filter(eventId = event_id).exists()

        if is_exists:
            event = Calendar.objects.filter(eventId = event_id)
            event.update(title=title)
            event.update(color=color)
            event.update(startDate = start_date)
            event.update(endDate = end_date)
            serialized_event = CalendarAllDataSerializer(event, many = True)
            return Response(serialized_event.data, status=200)
        else:
            return Response({'message': 'eventId is not exists'}, status=404)
        
## 캘린더 일정 제거
class DeleteCalendarView(APIView):
    def delete(slef,request,eventId):
        is_exist = Calendar.objects.filter(eventId = eventId).exists()
        
        if is_exist:
            event = Calendar.objects.filter(eventId = eventId)
            event.delete()
            return Response({'message':'deleted'},status=200)
        else:
            return Response({'message': 'eventId is not exists'}, status=404)

# Section 2 - 명부
# 전체 부원 불러오기
# function
## 0: 이름 오름차순, 1: 이름 내림차순, 2: 출석횟수 오름차순, 3: 출석횟수 내림차순, 4: 누적 봉사시간 오름차순, 5: 누적 봉사시간 내림차순, 6: 지각비 유무
### order, latencyCost, 
class GetnameListView(APIView):
    permission_classes = []
    @swagger_auto_schema(query_serializer=NameListSearchSerializer)
    def get(self,request):
        order = request.query_params.get('order')
        latency_cost = int(request.query_params.get('latencyCost'))
        name = request.query_params.get('name')
        school_id = request.query_params.get('school_id')

        if school_id:
            is_exist = Selslist.objects.filter(school_id__icontains = school_id).exists()
            if is_exist:
                namelist = Selslist.objects.filter(school_id__icontains = school_id).order_by(order)
            else:
                return Response({'message': '존재하지 않습니다.'}, status=404)
        else:
            if name:
                is_exist = Selslist.objects.filter(name__icontains = name).exists()
                if is_exist:
                    if (latency_cost > 0):
                        namelist = Selslist.objects.filter(name__icontains = name,latencyCost__gt = latency_cost).order_by(order)
                    else:
                        namelist = Selslist.objects.filter(name__icontains = name).order_by(order)
                else:
                    return Response({'message': '존재하지 않습니다.'}, status=404)
            else: 
                if (latency_cost > 0):
                    namelist = Selslist.objects.filter(latencyCost__gt = latency_cost).order_by(order)
                else:
                    namelist = Selslist.objects.order_by(order)
        
        serialized_selslist = NameSerializer(namelist,many = True)
        return Response(serialized_selslist.data,status=200)
        
## 부원 검색
# class GetOneNameView(APIView):
#     permission_classes = []
#     def get(self,request,name):
#         select_name = Selslist.objects.filter(name__icontains = name)
#         serialized_name = NameSerializer(select_name, many=True)
#         return Response(serialized_name.data,status=200)

## 부원 상세 정보 검색
# class GetOnedetailView(APIView):
#     def get(self,request,school_id):
#         select_user = Selslist.objects.filter(school_id = school_id)
#         if select_user:
#             serilized_name = NameSerializer(select_user,many=True)
#             return Response(serilized_name.data,status=200)
#         else:
#             return Response({'message':'It is not exists'},status=404)
    
## 부원 등록    
class PostNameListView(APIView):
    @swagger_auto_schema(request_body=post_selslist_params)
    def post(self,request):        
        add_name = NameSerializer(data=request.data)
        if add_name.is_valid():
            add_name.save()
            return Response(add_name.data, status=201)
        return Response(add_name.errors, status=400)

## 부원 수정
class UpdateNameListView(APIView):
    @swagger_auto_schema(request_body=post_selslist_params)
    def patch(self,request):
        name = request.data.get('name')
        is_admin = request.data.get('is_admin')
        sex = request.data.get('sex')
        school_id = request.data.get('school_id')
        department = request.data.get('department')
        attendance = request.data.get('attendance')
        accumulated_time = request.data.get('accumulated_time')
        accumulated_cost = request.data.get('accumulated_cost')
        latencyCost = request.data.get('latencyCost')
        
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
            return Response(serialized_user.data,status=200)
        else:
            return Response({'message': 'user is not exists'}, status=404)
## 전체 부원 삭제
class DeleteNameListView(APIView):
    @swagger_auto_schema(query_serializer=NameListRemoveSerializer)
    def delete(self,request):
        range = request.query_params.get('range')
        name = request.query_params.get('name')
        school_id = request.query_params.get('school_id')
        
        if range == all:
            data = Selslist.objects.all()
            if data.exists():
                data.delete()
                return Response('모든 데이터 삭제 완료',status=200)
            else:
                return Response('삭제하려는 데이터가 없습니다.',status=404)
        else:
            data = Selslist.objects.filter(school_id = school_id, name=name)
            is_exist = data.exists()
            if is_exist:
                data.delete()
                return Response('선택 부원 정보가 삭제되었습니다.',status=200) 
            else:
                return Response({'message': 'user is not exists'}, status=404)

# class DeleteAllNameListView(APIView):
#     def delete(self,request):
#         data = Selslist.objects.all()
#         data.delete()
#         return Response('모든 데이터가 삭제됬습니다.',status=200)
    
# class DeleteOneNameListView(APIView):
#     def delete(self,request,school_id,name):
#         data = Selslist.objects.filter(school_id = school_id, name=name)
#         is_exist = data.exists()
#         if is_exist:
#             data.delete()
#             return Response('선택 부원 정보가 삭제되었습니다.',status=200) 
#         else:
#             return Response({'message': 'user is not exists'}, status=404)

## 캘린더 일정에 명단 추가
class PostCalendarNameView(APIView):
    @swagger_auto_schema(request_body = post_calendar_name_parmas)
    def post(self,request):
        event_id = request.data.get('calendar_id')
        name = request.data.get('name')
        school_id = request.data.get('school_id')
        is_exists = Calendar.objects.filter(eventId = event_id).exists()
        if is_exists:
            add_name = Calendar_NameList(
               calendar_id = event_id,
               school_id = school_id,
               name = name,
               state_point = 0,
               state = 'default',
               attendanceTime =datetime.now()
            )
            add_name.save()
            serialized_name = CalendarNameListSerializer(add_name)
            return Response(serialized_name.data, status=201)       
        else:
            return Response({'message': 'eventId is not exists'}, status=404)
    
class UpdateCalendarNameView(APIView):
    @swagger_auto_schema(request_body = update_calendar_name_params)
    def patch(self,request):      
        event_id = request.data.get('eventId')
        name = request.data.get('name')
        school_id = request.data.get('school_id')
        state_point = request.data.get('state_point')
        state = request.data.get('state')
        attendanceTime = request.data.get('attendanceTime')

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
                return Response({'message': 'user is not exists'}, status=404)
        else: 
            return Response({'message': 'eventId is not exists'}, status=404)
class DeleteCalendarNameOneView(APIView):
    def delete(self,request,eventId, school_id):
        user = Calendar_NameList.objects.filter(school_id = school_id, calendar_id = eventId)
        user_exists = user.exists()
        if user_exists:
            user.delete()
            return Response('삭제 완료',status=200)
        else:
            return Response({'message': 'user is not exists'}, status=404)
class DeleteCalendarNameAllView(APIView):
    def delete(self,request,eventId):
        event = Calendar_NameList.objects.filter(calendar_id = eventId).all()
        event_exists = event.exists()
        if event_exists:
            event.delete()
            return Response('모든 데이터 삭제 완료')
        else:
            return Response('잘못된 명령입니다.')


## Section 4 : main function

