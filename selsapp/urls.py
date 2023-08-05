from django.urls import path
from . import views

urlpatterns = [    
    # django-swagger test
    path('v1/test/get',views.GetTestView.as_view(),name='test'),
    path('v1/test/post',views.PostTestView.as_view(),name='posttest'),

    # Calendar
    path('CalendarView/getAllCalendar',views.GetCalendarView.as_view(),name='getallcalendar'),
    path('CalendarView/getOneCalendar/<str:eventId>',views.GetCalendarOneView.as_view(),name='getonecalendar'),
    path('CalendarView/register',views.PostCalendarView.as_view(),name='postcalendar'),
    path('CalendarView/PostName',views.PostCalendarNameView.as_view(), name='postname'),
    
    # Namelist
    path('NameView/getAllName',views.GetnameListView.as_view(),name='getallname'),
    path('NameView/getName/<str:name>',views.GetOneNameView.as_view(),name='getonename'),
]

