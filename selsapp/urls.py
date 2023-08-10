from django.urls import path
from . import views

urlpatterns = [    
    # django-swagger test
    # path('v1/test/get',views.GetTestView.as_view(),name='test'),
    # path('v1/test/post',views.PostTestView.as_view(),name='posttest'),

    # Calendar
    path('calendar/all',views.GetCalendarAllView.as_view(),name='getallcalendar'),
    path('calendar/register',views.PostCalendarView.as_view(),name='postcalendar'),
    path('calendar/one/<str:eventId>',views.GetCalendarOneView.as_view(),name='getonecalendar'),
    path('calendar/<str:eventId>',views.DeleteCalendarView.as_view(),name='deleteonecalendar'),
    path('calendar',views.UpdateCalendarView.as_view(),name='updatecalendar'),

    # Namelist
    path('namelist/all',views.GetnameListView.as_view(),name='getallname'),
    path('namelist/register',views.PostNameListView.as_view(),name='postname'),
    path('namelist/<str:name>',views.GetOneNameView.as_view(),name='getonename'),
    path('namelist',views.UpdateNameListView.as_view(),name='updatename'),
    path('nameList/delete-all',views.DeleteAllNameListView.as_view(),name='deleteallname'),
    path('namelist/delete-one/<str:school_id>/<str:name>',views.DeleteOneNameListView.as_view(),name='deleteonename'),


    #path('namelist/register',views.PostNameListView.as_view(),name='postname'),
    
    # Calendar-name-list
    path('calendar-namelist/names',views.PostCalendarNameView.as_view(), name='postname'),
    path('calendar-namelist',views.UpdateCalendarNameView.as_view(),name = 'updatename'),
    path('calendar-namelist/one/<str:eventId>/<str:school_id>',views.DeleteCalendarNameOneView.as_view(),name = 'deleteonename'),
    path('calendar-namelist/all/<str:eventId>',views.DeleteCalendarNameAllView.as_view(),name = 'deleteallname'),
]

