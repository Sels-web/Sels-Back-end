from django.urls import path
from . import views

urlpatterns = [
    path('readdatas/', views.getTestDatas, name="test01datas"),
    path('postdatas/', views.postMember),
    path('putdatas/<str:pk>', views.putMember, name="putMember"),
    path('createList/<str:given_name>/<str:given_school_id>/<str:given_admin>', views.createList),
    path('deleteList/<str:given_name>/<str:given_school_id>', views.deleteList),
    path('readList', views.readList),
    path("update_admin/<str:given_name>/<str:given_admin>/<str:given_school_id>",views.update_admin),

]
