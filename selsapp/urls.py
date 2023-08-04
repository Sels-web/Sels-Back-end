from django.urls import path
from . import views
urlpatterns = [
#     ## test urls
#     path('readdatas/', views.getTestDatas, name="test01datas"),
#     path('postdatas/', views.postMember),
#     path('putdatas/<str:pk>', views.putMember, name="putMember"),
    
#     # 캘린더 CRUD
#     path('postCalendar',views.postCalendar), # 캘린더 생성
#     path('getOneCalendar',views.getOneCalendar), # 캘린더 하나 불러오기, 일정에 맞는 인원 불러오기와 합칠 예정
#         path('delteCalendar',views.deleteCalendar), # 캘린더 삭제하기

#     # 캘린더 인원 등록
#     path('getOneList',views.getOneList),
#     path('post-calendar-name/<str:calendar_id>/<str:school_id>/<str:name>/<str:state>/', views.postCalendarName), ## 캘린더에 출석 명단 등록하기

    # 일정에 맞는 인원 불러오기
    #path('getCalendarNameList/<str:calendar_id>',views.getCalendarNameList)

    # django-swagger test
    path('v1/test/',views.TestView.as_view(),name='test'),
    
    # Calendar
    path('calendarView',views.CalendarView.as_view(),name='getallcalendar')
    
]

