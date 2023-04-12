from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status   
from .models import Selslist,Calendar
from django.db.models import F,Sum, Count, Case, When
from .serializers import TestDataSerializer,CalendarDataSerializer
from django.http import JsonResponse
import json as JSON

def calendarToDictionary(calendar):
   
    output = {}
    output["title"] = calendar.title
    output["startDate"] = calendar.startDate
    output["endDate"] = calendar.endDate
    output["color"] = calendar.color
    output["eventId"] = calendar.eventId
    output["enterNames"] = calendar.enterNames

    return output 

def selslistToDictionary(selslist):
   
    output = {}
    output["school_id"] = selslist.school_id
    output["name"] = selslist.name
    output["is_admin"] = selslist.is_admin
    output["attendance"] = selslist.attendance
    output["accumulated_time"] = selslist.accumulated_time
    output["latencyCost"] = selslist.latencyCost

    return output 

@api_view(['GET'])
def getTestDatas(request):
    datas = Selslist.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postMember(request):
    reqData = request.data
    serializer = TestDataSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def putMember(request, pk):
    reqData = request.data
    data = Selslist.objects.get(id=pk)
    serializer = TestDataSerializer(instance=data, data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postCalendar(request):
    order = (JSON.loads(request.body.decode('utf-8')))
    is_exists = Calendar.objects.filter(eventId = order["eventId"]).exists()
    
    if is_exists:
        return HttpResponse("It exists")
    else:
        print(order)
        newObject = Calendar.objects.create(title=order["title"], startDate=order["start"], endDate = order["end"], color = order["color"], eventId = order["eventId"])
        newObject.save()
        return HttpResponse("Good!")

@api_view(['GET'])
def getOneCalendar(request):
    order = (JSON.loads(request.body.decode('utf-8')))
    is_exists = Calendar.objects.filter(eventId = order["eventId"]).exists()

    if is_exists:
        order_qs = Calendar.objects.filter(eventId = order["eventId"])
        return HttpResponse(order_qs)
    else:
        return HttpResponse("No Calendar")

@api_view(['GET'])
def getAllCalendar(request):
    order_qs = Calendar.objects.all()
    temp = []
    for i in range(len(order_qs)):
        temp.append(calendarToDictionary(order_qs[i]))
    orders = temp
    data = {
        "orders":orders
    }
    return JsonResponse(data)

@api_view(['PUT'])
def deleteCalendar(request):
    order = (JSON.loads(request.body.decode('utf-8')))
    is_exists = Calendar.objects.filter(eventId = order["eventId"]).exists()

    if is_exists:
        order_qs = Calendar.objects.filter(eventId = order["eventId"]).delete()
        order_qs.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("No Calendar")
    
@api_view(['GET'])
def getOneList(request,g_name):

    order = (JSON.loads(request.body.decode('utf-8')))
    is_exists = Selslist.objects.filter(name = order["name"]).exists()

    if is_exists:
        order_qs = Selslist.objects.filter(name = order["name"]).values()
        return HttpResponse(order_qs)
    else:
        return HttpResponse("No one that name")