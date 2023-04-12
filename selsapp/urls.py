from django.urls import path
from . import views

urlpatterns = [
    path('readdatas/', views.getTestDatas, name="test01datas"),
    path('postdatas/', views.postMember),
    path('putdatas/<str:pk>', views.putMember, name="putMember"),
    
    # 캘린더 CRUD
    path('postCalendar',views.postCalendar),
    path('getOneCalendar',views.getOneCalendar),
    path('getAllCalendar',views.getAllCalendar),
    path('delteCalendar',views.deleteCalendar),

    # 캘린더 인원 등록
    path('getOneList/<str:g_name>',views.getOneList),
]
