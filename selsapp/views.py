from django.shortcuts import render, HttpResponse

from rest_framework.decorators import api_view
from rest_framework import status   
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Selslist,Calendar,Calendar_NameList
from django.db.models import F,Sum, Count, Case, When
from django.http import JsonResponse
import json as JSON

from .serializers import TestDataSerializer,CalendarAllDataSerializer

from .open_api_params import get_params,post_params

class TestView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(manual_parameters=get_params)
    def get (self,request):
        return Response("Swagger Testing")
    
    @swagger_auto_schema()
    def post(self,request):
        return Response("Swagger Schema")


# @api_view(['POST'])
# def postCalendar(request):
#     order = (JSON.loads(request.body.decode('utf-8')))
#     is_exists = Calendar.objects.filter(eventId = order["eventId"]).exists()
#     if is_exists:
#         return HttpResponse("It exists")
#     else:
#         newObject = Calendar.objects.create(
#             title=order["title"], 
#             startDate=order["start"], 
#             endDate = order["end"], 
#             color = order["color"], 
#             eventId = order["eventId"]
#         )
#         newObject.save()
#         return HttpResponse("Good!")
class CalendarView(APIView):
    # Section 1 - 캘린더
    ## 모든 캘린더 불러오기 
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        calendar_events = Calendar.objects.all()
        serialized_calendar = CalendarAllDataSerializer(calendar_events, many=True)
        return Response(serialized_calendar.data)
    
    @swagger_auto_schema(manual_parameters=post_params)
    def post(self,request):
        title = request.query_params.get('title')
        color = request.query_params.get('Color')
        event_id = request.query_params.get('eventId')
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')

        event = Calendar(
            title=title,
            color=color,
            eventId=event_id,
            startDate=start_date,
            endDate=end_date
        )
        event.save()

        return Response('success!')

    
# @api_view(['GET'])

# def getAllCalendar(request):
        # order_qs = Calendar.objects.all()
#         temp = []
#         for i in range(len(order_qs)):
#             temp.append(calendarToDictionary(order_qs[i]))
#         orders = temp
#         data = {
#             "orders":orders
#         }
#         return JsonResponse(data)

# def calendarToDictionary(calendar):
#     output = {}
#     output["title"] = calendar.title
#     output["startDate"] = calendar.startDate
#     output["endDate"] = calendar.endDate
#     output["color"] = calendar.color
#     output["eventId"] = calendar.eventId
#     output["enterNames"] = calendar.enterNames
#     return output 

# def calendarNameListToDictionary(calendar_NameList):   
#     output = {}
#     output["calendar_id"] = calendar_NameList.title
#     output["school_id"] = calendar_NameList.startDate
#     output["name"] = calendar_NameList.endDate
#     output["state_point"] = calendar_NameList.color
#     output["state"] = calendar_NameList.eventId
#     output["attendanceTime"] = calendar_NameList.enterNames
#     return output 

# def selslistToDictionary(selslist):
#     output = {}
#     output["school_id"] = selslist.school_id
#     output["name"] = selslist.name
#     output["is_admin"] = selslist.is_admin
#     output["attendance"] = selslist.attendance
#     output["accumulated_time"] = selslist.accumulated_time
#     output["latencyCost"] = selslist.latencyCost
#     output["accumulated_cost"]=selslist.accumulated_cost
#     output["department"]=selslist.department
#     output["sex"]=selslist.sex
#     return output 

# ## Data Testing by rest_frame
# @api_view(['GET'])
# def getTestDatas(request):
#     datas = Selslist.objects.all()
#     serializer = TestDataSerializer(datas, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def postMember(request):
#     reqData = request.data
#     serializer = TestDataSerializer(datpipa=reqData)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def putMember(request, pk):
#     reqData = request.data
#     data = Selslist.objects.get(id=pk)
#     serializer = TestDataSerializer(instance=data, data=reqData)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# ## 캘린더 세부 일정 불러오기
# @api_view(['GET'])
# def getOneCalendar(request):
#     order = (JSON.loads(request.body.decode('utf-8')))
#     is_exists = Calendar.objects.filter(eventId = order["eventId"]).exists()
#     if is_exists:
#         temp = []
#         calendar_info = Calendar.objects.filter(eventId = order["eventId"]).values()
#         temp.append(calendarToDictionary(calendar_info))
#         user_info = Calendar_NameList.objects.filter(calendar_id = order["eventId"]).all()
#         for i in range(len(user_info)):
#             temp.append(user_info[i])
#         orders = temp
#         data = {
#             "order": orders
#         }
#         return JsonResponse(data)
#     else:
#         return HttpResponse("No Calendar")
    
# # 일정에 저장된 이름 가져오기
# # @api_view(['GET'])
# # def getCalendarNameList(request,calendar_id):
# #     is_exists = Calendar.objects.filter(eventId = calendar_id).exists()
# #     if is_exists:
# #         order_qs = Calendar_NameList.objects.filter(calendar_id = calendar_id).values()
# #         return HttpResponse(order_qs)
# #     else:
# #         return HttpResponse("No Calendar")

# ## 일정 1개에 출석부 명단 - 참여 인원 DB등록
# def postCalendarName(request,calendar_id,school_id,name,state):
#     # request로부터 받은 데이터로 새로운 인스턴스 생성
#     instance = Calendar_NameList.objects.create(
#         calendar_id = calendar_id,
#         school_id=school_id,
#         name=name,
#         state=state,
#         state_point=0, # state_point 기본값으로 0 설정
#     )
#     serialized_data = {
#         'school_id': instance.school_id,
#         'name': instance.name,
#         'state_point': instance.state_point,
#         'state': instance.state,
#         'attendanceTime': instance.attendanceTime,
#         'calendar_id': instance.calendar_id,
#     }
#     return HttpResponse(serialized_data) 

# ## 일정 삭제 
# # input: eventId
# # ouput: x
# @api_view(['PUT'])
# def deleteCalendar(request):
#     order = (JSON.loads(request.body.decode('utf-8')))
#     is_exists = Calendar.objects.filter(eventId = order["eventId"]).exists()
#     if is_exists:
#         order_qs = Calendar.objects.filter(eventId = order["eventId"]).delete()
#         order_qs.save()
#         return HttpResponse("Success!")
#     else:
#         return HttpResponse("No Calendar")
    
# ## 이름 하나 불러오기
# @api_view(['POST'])
# def getOneList(request):
#     order = (JSON.loads(request.body.decode('utf-8')))
#     is_exists = Selslist.objects.filter(name = order["Username"]).exists()
#     if is_exists:
#         order_qs = Selslist.objects.filter(name = order["Username"]).values()
#         return HttpResponse(order_qs)
#     else:
#         return HttpResponse("No one that name") 