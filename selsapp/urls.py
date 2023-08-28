from django.urls import path
from . import views

urlpatterns = [    
    # Calendar
    ## CREATE
    path('calendar/register',views.PostCalendarView.as_view(),name='postcalendar'), # 캘린더 등록하기
    ## READ
    path('calendar/search',views.GetCalendarAllView.as_view(),name='getallcalendar'), # 모든 캘린더 불러오기
    # path('calendar/one/<str:eventId>',views.GetCalendarOneView.as_view(),name='getonecalendar'), #캘린더 아이디로 캘린더 불러오기
    # path('calendar/month',views.GetCalendarMonthView.as_view(),name='getmonthcalendar'), # 현재 월에 해당하는 캘린더 가져오기
    ## UPDATE
    path('calendar',views.UpdateCalendarView.as_view(),name='updatecalendar'), # 캘린더 수정하기
    ## DELETE
    path('calendar/<str:eventId>',views.DeleteCalendarView.as_view(),name='deleteonecalendar'), # 캘린더 삭제하기(한개)

    # Namelist
    ## CREATE
    path('namelist/register',views.PostNameListView.as_view(),name='postname'), # 명단 등록하기
    ## READ
    path('namelist/search',views.GetnameListView.as_view(),name='getallname'), # 전체 명단 불러오기 by function key
    ## UPDATE
    path('namelist/update',views.UpdateNameListView.as_view(),name='updatename'), # 명단 수정하기
    ## DELETE
    path('namelist/delete',views.DeleteNameListView.as_view(),name='deletename'), # 모든 명단 삭제하기
    
    # Calendar-name-list
    ## CREATE
    path('calendar-namelist/register',views.PostCalendarNameView.as_view(), name='postname'), # 캘린더 일정에 참석자 등록하기
    ## READ
    path('calendar-namelist/search/<str:eventId>',views.GetCalendarNameView.as_view(), name='getnamelist'), # 캘린더 일정에 참석자 불러오기
    ## UPDATE
    path('calendar-namelist',views.UpdateCalendarNameView.as_view(),name = 'updatename'), # 캘린더 일정 참석자 수정하기
    ## DELETE
    path('calendar-namelist/',views.DeleteCalendarNameView.as_view(),name = 'deletename'), # 참석자 제거

    ## main function
    path('attendance',views.attendanceManageView.as_view(),name='attendanceManage'),
    
    path('calculation/<str:event_id>',views.CalculateManagementView.as_view(),name='calculateManage'),

    ## reference 
    path('reference/register',views.PostReferenceView.as_view(),name='postreferencetable'),
    path('reference/search',views.GetReferenceView.as_view(),name='getreferencetable'),
    path('reference/update',views.UpdateReferenceView.as_view(),name='updatereferencetable'),
    path('reference/delete',views.DeleteReferenceView.as_view(),name='deletereference'),
]

