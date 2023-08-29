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

                if serialized_event:
                    return Response(serialized_event.data,status=200)
                else:
                    return Response({'message': 'eventId is not exists'}, status=404)
                
            elif range == 'month':
                now = datetime.now()
                querymonth = now.strftime('%Y-%m')
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
        title = request.data.get('title')
        color = request.data.get('color')
        event_id = request.data.get('eventId')
        start_date = request.data.get('startDate')
        end_date = request.data.get('endDate')

        format_str = '%Y-%m-%dT%H:%M'
        format_str_second = '%Y-%m-%dT%H:%M:%S'

        if len(start_date)== 16 and len(end_date)== 16:
            start_date_obj = datetime.strptime(start_date, format_str)  
            end_date_obj = datetime.strptime(end_date, format_str)   

        elif len(start_date)== 19 and len(end_date) == 16:
            start_date_obj = datetime.strptime(start_date, format_str_second)  
            end_date_obj = datetime.strptime(end_date, format_str)     

        elif len(start_date)== 16 and len(end_date) == 19:
            start_date_obj = datetime.strptime(start_date, format_str)  
            end_date_obj = datetime.strptime(end_date, format_str_second)     

        elif len(start_date)== 19 and len(end_date) == 16:
            start_date_obj = datetime.strptime(start_date, format_str_second)  
            end_date_obj = datetime.strptime(end_date, format_str_second)


        activity_time = end_date_obj - start_date_obj
        activity_hours = int(activity_time.total_seconds() // 3600)
        
        if Calendar.objects.filter(eventId=event_id).exists():
            return Response({'message': 'eventId already exists'}, status=400)
        else:
            event = Calendar(
                title = title,
                color = color,
                startDate = start_date,
                endDate = end_date,
                eventId = event_id,
                activity_time = activity_hours,
            )
            event.save()
            serialized_event = CalendarAllDataSerializer(event)
            return Response(serialized_event.data,status=201)

## 캘린더 일정 수정
class UpdateCalendarView(APIView):
    @swagger_auto_schema(request_body = update_calendar_params)
    def patch(self,request):
        title = request.data.get('title')
        color = request.data.get('color')
        event_id = request.data.get('eventId')
        start_date = request.data.get('startDate')
        end_date = request.data.get('endDate')

        format_str = '%Y-%m-%dT%H:%M'
        format_str_second = '%Y-%m-%dT%H:%M:%S'

        if len(start_date)== 16 and len(end_date)== 16:
            start_date_obj = datetime.strptime(start_date, format_str)  
            end_date_obj = datetime.strptime(end_date, format_str)   

        elif len(start_date)== 19 and len(end_date) == 16:
            start_date_obj = datetime.strptime(start_date, format_str_second)  
            end_date_obj = datetime.strptime(end_date, format_str)     

        elif len(start_date)== 16 and len(end_date) == 19:
            start_date_obj = datetime.strptime(start_date, format_str)  
            end_date_obj = datetime.strptime(end_date, format_str_second)     

        elif len(start_date)== 19 and len(end_date) == 16:
            start_date_obj = datetime.strptime(start_date, format_str_second)  
            end_date_obj = datetime.strptime(end_date, format_str_second)

        activity_time = end_date_obj - start_date_obj
        activity_hours = int(activity_time.total_seconds() // 3600)

        is_exists = Calendar.objects.filter(eventId = event_id).exists()

        if is_exists:
            event = Calendar.objects.filter(eventId = event_id)
            event.update(title=title)
            event.update(color=color)
            event.update(startDate = start_date)
            event.update(endDate = end_date)
            event.update(activity_time = activity_hours)
            namelist= Calendar_NameList.objects.filter(calendar_id = event_id)

            for name in namelist:
                name.service_time = activity_hours
                name.save()
            serialized_event = CalendarAllDataSerializer(event, many=True)
            return Response(serialized_event.data, status=200)
        else:
            return Response({'message': 'eventId is not exists'}, status=404)
## 캘린더 일정 제거
class DeleteCalendarView(APIView):
    def delete(slef,request,eventId):
        is_exist = Calendar.objects.filter(eventId = eventId).exists()
        
        if is_exist:
            event = Calendar.objects.filter(eventId = eventId)
            namelist = Calendar_NameList.objects.filter(calendar_id = eventId)
            if namelist.exists():
                event.delete()
                namelist.delete()
            else:
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
        latency_cost = request.query_params.get('latencyCost')
        name = request.query_params.get('name')
        school_id = request.query_params.get('school_id')

        if school_id:   # 학번 검색
            is_exist = Selslist.objects.filter(school_id__icontains = school_id).exists()
            if is_exist:
                namelist = Selslist.objects.filter(school_id__icontains = school_id).order_by(order)
            else:
                return Response({'message': '존재하지 않는 학번입니다.'}, status=404)
        else:   
            if name: # 이름 검색
                is_exist = Selslist.objects.filter(name__icontains = name).exists()
                if is_exist:
                    namelist = Selslist.objects.filter(name__icontains = name).order_by(order)
                else:
                    namelist = Selslist.objects.filter(name__icontains = name).order_by(order)
            elif latency_cost:
                namelist = Selslist.objects.filter(latencyCost__gt = 0).order_by(order)
            elif (latency_cost and name):
                is_exist = Selslist.objects.filter(name__icontains = name,latency_cost = 0).exists()
                if is_exist:
                    namelist = Selslist.objects.filter(name__icontains = name,latency_cost = 0).order_by(order)
                else:
                    namelist = Selslist.objects.filter(name__icontains = name,latency_cost = 0).order_by(order)
            else: 
                namelist = Selslist.objects.all().order_by(order)
                for name in namelist:   # 전체 이름 조회로 전부다 수행
                    participant_events = Calendar_NameList.objects.filter(school_id = name.school_id)
                    participant = participant_events.first()
                    if participant_events.exists():
                        # 참석 횟수
                        name.attendance = participant_events.exclude(Q(state=0)|Q(state=4)).count()
                        # 총 봉사시간
                        if participant.state == 0 or participant.state ==4:
                            participant.service_time = 0
                            participant.save()

                        total_service_time = participant_events.aggregate(total_service_time=Sum('service_time'))['total_service_time']
                        name.accumulated_time = total_service_time

                        # 지각비
                        total_late_cost = participant_events.aggregate(total_late_cost=Sum('latency_cost'))['total_late_cost']
                        name.latencyCost = total_late_cost

                        #경고 횟수
                        name.penalty_cnt = participant_events.filter(penalty = 1).count()  
                        name.save()
                    else:
                        name.attendance = 0
                        name.accumulated_time = 0
                        name.accumulated_cost = 0
                        name.latencyCost = 0
                        name.penalty_cnt = 0
                        name.save()

        
        serialized_selslist = NameSerializer(namelist,many = True)
        return Response(serialized_selslist.data,status=200)
        
## 부원 등록    
class PostNameListView(APIView):
    @swagger_auto_schema(request_body=post_selslist_params)
    def post(self,request):        
        name = request.data.get('name')
        is_admin = request.data.get('is_admin')
        sex = request.data.get('sex')
        school_id = request.data.get('school_id')
        department = request.data.get('department')

        if Selslist.objects.filter(school_id=school_id).exists():
            return Response({'message': 'school already exists'}, status=400)
        else:
            user = Selslist(
              name = name,
              is_admin = is_admin,
              sex = sex,
              school_id = school_id,
              department = department,
              attendance = 0,
              accumulated_time = 0,
              accumulated_cost = 0,
              latencyCost = 0, 
              penalty_cnt = 0,
            )
            user.save()
            serialized_user = NameSerializer(user)
            return Response(serialized_user.data,status=201)

## 부원 수정
class UpdateNameListView(APIView):
    @swagger_auto_schema(request_body=update_selslist_params)
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
        penalty_cnt = request.data.get('penalty_cnt')

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
            user.update(penalty_cnt = penalty_cnt)
            
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

        if range == 'all':
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

## 캘린더 일정에 명단 추가
class PostCalendarNameView(APIView):
    @swagger_auto_schema(request_body = post_calendar_name_parmas)
    def post(self,request):
        event_id = request.data.get('calendar_id')
        name = request.data.get('name')
        school_id = request.data.get('school_id')
        
        event = Calendar.objects.filter(eventId = event_id)
        event_info = event.first()

        if event.exists():
            add_name = Calendar_NameList(
               calendar_id = event_id,
               school_id = school_id,
               name = name,
               state = 0,
               late_time = 'default',
               attendanceTime =event_info.startDate,
               latency_cost = 0,
               service_time = 0,
               penalty = 0,
               calculated = 0,
            )
            add_name.save()
            serialized_name = CalendarNameListSerializer(add_name)
            return Response(serialized_name.data, status=201)       
        else:
            return Response({'message': 'eventId is not exists'}, status=404)
class GetCalendarNameView(APIView):
    def get(self,request,eventId):
        namelist = Calendar_NameList.objects.filter(calendar_id = eventId)     
        serailized_namelist = CalendarNameListSerializer(namelist,many=True)
        return Response(serailized_namelist.data, status=200)

## 수정필요-2023.08.25 / 수정완료
class UpdateCalendarNameView(APIView):
    @swagger_auto_schema(request_body = update_calendar_name_params)
    def patch(self,request):      
        event_id = request.data.get('eventId')
        name = request.data.get('name')
        school_id = request.data.get('school_id')
        attendanceTime = request.data.get('attendanceTime')

        event = Calendar.objects.filter(eventId = event_id).first()
        start_time = event.startDate ## 시작 시간 저장

        participant = Calendar_NameList.objects.filter(school_id=school_id,calendar_id = event_id)

        participant.update(name=name)

        current_time = datetime.strptime(attendanceTime, '%Y-%m-%dT%H:%M:%S')

        ## 지각비 정산 helper
        latetime = current_time - start_time ## 지각한 시간
        latetime_second = int(latetime.total_seconds())

        if(latetime_second <=0):
            latetime_str = '0:00:00'
        
        else:
            ## state helper
            hours = latetime.seconds // 3600  # 초를 시간 단위로 변환
            minutes = (latetime.seconds // 60) % 60  # 초를 분 단위로 변환
            seconds = latetime.seconds % 60

            latetime_str = f"{hours}:{minutes}:{seconds}"

        if (latetime_second<=0):

            participant.update(state=1)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 0)
            participant.update(penalty = 0)
            participant.update(service_time = event.activity_time)
            
        elif (latetime_second>0 and latetime_second < 60): # 지각X:

            participant.update(state=1)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 0)
            participant.update(penalty = 0)
            participant.update(service_time = event.activity_time)

        elif (latetime_second >=60 and latetime_second <660): # 1-10분 지각

            participant.update(state=2)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 1000)
            participant.update(penalty = 0)
            participant.update(service_time = event.activity_time)
        
        elif (latetime_second>=660 and latetime_second <1800): # 11분 이상 지각
            participant.update(state=3)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 3000)
            participant.update(penalty = 0)
            service_time = event.activity_time -1
            participant.update(service_time = service_time)
    
        elif(latetime_second >=1800):
            participant.update(state=4)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 5000)
            participant.update(penalty = 1)
            participant.update(service_time =0)

        return Response('complete',status=200)

class DeleteCalendarNameView(APIView):
    @swagger_auto_schema(query_serializer=CalendarNamelistRemoveSerializer)
    def delete(self,request):
        range = request.query_params.get('range')
        event_id = request.query_params.get('event_id')
        school_id = request.query_params.get('school_id')

        if range =='all':
            namelist = Calendar_NameList.objects.filter(calendar_id = event_id)
            if namelist.exists():
                namelist.delete()
                return Response({'message': '해당 참석자 전원 삭제 완료'},status=200)
            else:
                return Response({'message': 'event_id erros'},status=404)
        elif range == 'one':
            namelist = Calendar_NameList.objects.filter(calendar_id = event_id,school_id = school_id)
            if namelist.exists():
                namelist.delete()
                return Response({'message': '해당 참석자 삭제 완료'},status=200)
            else:
                return Response({'message': 'event_id erros'},status=404)


## Section 3 : reference table
class PostReferenceView(APIView):
    @swagger_auto_schema(request_body = post_reference_params)
    def post(self,request):
        title = request.data.get('title')
        upload_date_str = request.data.get('upload_date')
        content = request.data.get('content')

        upload_date= datetime.strptime(upload_date_str,'%Y-%m-%dT%H:%M')
        
        new_posts = Reference(
                title = title,
                upload_date = upload_date,
                content = content,
            )
        new_posts.save()
        serialized_posts = ReferenceSerializer(new_posts)
        return Response(serialized_posts.data,status=201)

class GetReferenceView(APIView):
    @swagger_auto_schema(query_serializer=ReferenceSearchSerializer)
    def get(self, request):
        range = request.query_params.get('range')
        id = request.query_params.get('id')

        if range == 'all':
            posts = Reference.objects.all()
            if posts.exists():
                serialized_posts = ReferenceSerializer(posts, many=True)
                return Response(serialized_posts.data, status=200)
            else:
                return Response({'message': '게시물이 존재 하지 않습니다'}, status=404)
            
        elif range == 'one':
            post = Reference.objects.filter(id = id)
            if post.exists():
                serialized_post = ReferenceSerializer(post, many=True)
                return Response(serialized_post.data,status=200)
            else:
                return Response({'message': '해당하는 게시물을 찾을 수 없습니다.'}, status=404)

class UpdateReferenceView(APIView):
    @swagger_auto_schema(request_body=update_reference_params)
    def patch(self,request):
        id = request.data.get('id')
        title = request.data.get('title')
        upload_date_str = request.data.get('upload_date')
        content = request.data.get('content')

        upload_date= datetime.strptime(upload_date_str,'%Y-%m-%dT%H:%M')

        post = Reference.objects.filter(id=id)
        if post.exists():
            post.update(title=title)
            post.update(upload_date = upload_date)
            post.update(content = content)
            serialized_post = ReferenceSerializer(post, many=True)
            return Response(serialized_post.data, status=200)
        else:
            return Response({'message': '해당하는 게시물을 찾을 수 없습니다.'},status=404)

class DeleteReferenceView(APIView):
    @swagger_auto_schema(query_serializer=ReferenceRemoveSerializer)
    def delete(self, request):
        range = request.query_params.get('range')
        id = request.query_params.get('id')

        if range=='all':
            posts = Reference.objects.all()
            if posts.exists():
                posts.delete()
                return Response({'message': '모든 데이터 삭제 완료'},status=200)
            else:
                return Response({'message': '삭제할 게시물이 존재하지 않습니다.'},status=404)
        elif range=='one':
            post = Reference.objects.filter(id=id)
            if post.exists():
                post.delete()
                return Response({'message': '해당하는 게시물을 삭제헀습니다.'},status=200)
            else:
                return Response({'message': '삭제할 게시물이 존재하지 않습니다.'},status=404)
## Section 4 : main function
# patch 
# input: eventId, 요청한 현재 시간, school_id
# function : 
# calendar_namelist:  state_point, state, attendanceTime
# selslist: latencyCost 계산 및 누적 지각비 계산,attendance 출석 횟수 증가, accumulated_time, accumulated_cost
# 지각비 계산하기 위해 출석 시간 찍히도록 변수 저장

## 수정필요-2023.08.25 / 수정완료
class attendanceManageView(APIView):
    @swagger_auto_schema(request_body=post_attendance_params)
    def post(self, request):
        event_id = request.data.get('event_id')
        current_time_str = request.data.get('current_time')
        school_id = request.data.get('school_id')

        event = Calendar.objects.filter(eventId = event_id).first()
        print(event.eventId)
        start_time = event.startDate ## 시작 시간 저장

        participant = Calendar_NameList.objects.filter(school_id=school_id,calendar_id = event_id)

        current_time = datetime.strptime(current_time_str, '%Y-%m-%dT%H:%M:%S')
        ## 지각비 정산 helper
        latetime = current_time - start_time ## 지각한 시간
        latetime_second = int(latetime.total_seconds())

        if(latetime_second <=0):
            latetime_str = '0:00:00'
        
        else:
            ## state helper
            hours = latetime.seconds // 3600  # 초를 시간 단위로 변환
            minutes = (latetime.seconds // 60) % 60  # 초를 분 단위로 변환
            seconds = latetime.seconds % 60

            latetime_str = f"{hours}:{minutes}:{seconds}"

        if (latetime_second<=0):

            participant.update(state=1)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 0)
            participant.update(penalty = 0)
            participant.update(service_time = event.activity_time)
            
        elif (latetime_second>0 and latetime_second < 60): # 지각X:

            participant.update(state=1)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 0)
            participant.update(penalty = 0)
            participant.update(service_time = event.activity_time)

        elif (latetime_second >=60 and latetime_second <660): # 1-10분 지각

            participant.update(state=2)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 1000)
            participant.update(penalty = 0)
            participant.update(service_time = event.activity_time)
        
        elif (latetime_second>=660 and latetime_second <1800): # 11분 이상 지각
            participant.update(state=3)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 3000)
            participant.update(penalty = 0)
            service_time = event.activity_time -1
            participant.update(service_time = service_time)
    
        elif(latetime_second >=1800):
            participant.update(state=4)
            participant.update(late_time = latetime_str)
            participant.update(attendanceTime = current_time)
            participant.update(latency_cost = 5000)
            participant.update(penalty = 1)
            participant.update(service_time =0)

        return Response('complete',status=200)
    
# 정산하기
class CalculateManagementView(APIView):
    def patch(self,request):
        latecomer_list = Selslist.objects.filter(latencyCost__gt =0)
        for latecomer in latecomer_list:
            latecomer_info = Calendar_NameList.objects.filter(school_id = latecomer.school_id).first()
            
            latecomer.accumulated_cost = latecomer.accumulated_cost + latecomer_info.latency_cost            
            latecomer.save()

            latecomer_info.latency_cost =0
            latecomer_info.calculated = 1
            latecomer_info.save()
        return Response({'message':'completed'})