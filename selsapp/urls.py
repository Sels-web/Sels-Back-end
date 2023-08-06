from django.urls import path
from . import views

urlpatterns = [    
    # django-swagger test
    path('v1/test/get',views.GetTestView.as_view(),name='test'),
    path('v1/test/post',views.PostTestView.as_view(),name='posttest'),

    # Calendar
    path('CalendarView/getAllCalendar',views.GetCalendarAllView.as_view(),name='getallcalendar'),
    path('CalendarView/getOneCalendar/<str:eventId>',views.GetCalendarOneView.as_view(),name='getonecalendar'),
    path('CalendarView/register',views.PostCalendarView.as_view(),name='postcalendar'),
    path('CalendarView/PostName',views.PostCalendarNameView.as_view(), name='postname'),
    path('CalendarView/deleteOneCalendar/<str:eventId>',views.DeleteCalendarView.as_view(),name='deleteonecalendar'),
    path('CalendarView/updateCalendar',views.UpdateCalendarView.as_view(),name='updatecalendar'),
    
    # Namelist
    path('NameView/getAllName',views.GetnameListView.as_view(),name='getallname'),
    path('NameView/getName/<str:name>',views.GetOneNameView.as_view(),name='getonename'),
    path('NameView/regist',views.PostNameListView.as_view(),name='postname'),
    path('NameView/update',views.UpdateNameListView.as_view(),name='updatename'),
    path('NameView/deleteall',views.DeleteAllNameListView.as_view(),name='deleteallname'),
    path('NameView/deleteone/<str:school_id>/<str:name>',views.DeleteOneNameListView.as_view(),name='deleteonename'),


]

