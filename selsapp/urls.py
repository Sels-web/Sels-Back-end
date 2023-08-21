from django.urls import path
from . import views

urlpatterns = [    
    # django-swagger test
    # path('v1/test/get',views.GetTestView.as_view(),name='test'),
    # path('v1/test/post',views.PostTestView.as_view(),name='posttest'),

    # Calendar
    path('calendar/all',views.GetCalendarAllView.as_view(),name='getallcalendar'), # 모든 캘린더 불러오기
    path('calendar/register',views.PostCalendarView.as_view(),name='postcalendar'), # 캘린더 등록하기
    path('calendar/one/<str:eventId>',views.GetCalendarOneView.as_view(),name='getonecalendar'), #캘린더 아이디로 캘린더 불러오기
    path('calendar/month',views.GetCalendarMonthView.as_view(),name='getmonthcalendar'), # 현재 월에 해당하는 캘린더 가져오기
    path('calendar/<str:eventId>',views.DeleteCalendarView.as_view(),name='deleteonecalendar'), # 캘린더 삭제하기(한개)
    path('calendar',views.UpdateCalendarView.as_view(),name='updatecalendar'), # 캘린더 수정하기

    # Namelist
    path('namelist/all/<int:function>',views.GetnameListView.as_view(),name='getallname'), # 전체 명단 불러오기 by function key
    path('namelist/register',views.PostNameListView.as_view(),name='postname'), # 명단 등록하기
    path('namelist/<str:name>',views.GetOneNameView.as_view(),name='getonename'), # 이름으로 검색
    # path('namelist',views.UpdateNameListView.as_view(),name='updatename'), # 명단 수정하기
    path('namelist/delete-one/<str:school_id>/<str:name>',views.DeleteOneNameListView.as_view(),name='deleteonename'), # 명단 삭제하기

    path('nameList/delete-all',views.DeleteAllNameListView.as_view(),name='deleteallname'), # 모든 명단 삭제하기
    
    # Calendar-name-list
    path('calendar-namelist/names',views.PostCalendarNameView.as_view(), name='postname'), # 캘린더 일정에 참석자 등록하기
    path('calendar-namelist',views.UpdateCalendarNameView.as_view(),name = 'updatename'), # 캘린더 일정 참석자 수정하기
    # 캘린더 일정 참석자 한명 제거
    path('calendar-namelist/one/<str:eventId>/<str:school_id>',views.DeleteCalendarNameOneView.as_view(),name = 'deleteonename'), 
    path('calendar-namelist/all/<str:eventId>',views.DeleteCalendarNameAllView.as_view(),name = 'deleteallname'), # 모든 참석자 제거
]

