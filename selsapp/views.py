from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status   
from .models import Selslist
from django.db.models import F,Sum, Count, Case, When
from .serializers import TestDataSerializer

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


def createList(request,given_name,given_school_id,given_admin):
    is_exists = Selslist.objects.filter(name=given_name, school_id = given_school_id).exists()
    if is_exists:
        return HttpResponse("It's exists member. please check your List")
    else:
        newObject = Selslist.objects.create(name=given_name, school_id = given_school_id, is_admin = given_admin)
        newObject.save()
        return HttpResponse("created!")
    
def deleteList(request, given_name,given_school_id):
    is_exists = Selslist.objects.filter(name=given_name,school_id = given_school_id).exists()
    if is_exists:
        Selslist.objects.filter(name=given_name, school_id = given_school_id).delete()
        return HttpResponse("Deleted!")
    else:
        return HttpResponse("Don't exists! Check your List!")    
    
def readList(request):
    order_qs = Selslist.objects.all().values_list(
        'name', 'is_admin'
    )
    return HttpResponse(order_qs)

def update_admin(request,given_name,given_admin,given_school_id):
    is_exists = Selslist.objects.filter(name=given_name, school_id = given_school_id).exists()

    if is_exists:
        order_qs = Selslist.objects.filter(name=given_name, school_id = given_school_id)
        order_qs.update(is_admin = given_admin)
        return HttpResponse("Updated your admin access!")
    else:
        return HttpResponse("Don't exists name! Check your List")

