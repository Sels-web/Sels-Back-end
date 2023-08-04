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