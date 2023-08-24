from drf_yasg import openapi
from .models import *
from datetime import datetime

# ## 캘린더 일정 등록
# # input: JSON(title, startDate, endDate, Color, evnetId)
# # output: x

## Calendar
post_calendar_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the event'),
        'color': openapi.Schema(type=openapi.TYPE_STRING, description='Color of the event'),
        'eventId': openapi.Schema(type=openapi.TYPE_STRING, description='Event ID'),
        'startDate': openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_DATETIME, default=datetime.now().strftime('%Y-%m-%dT%H:%M'),description='시작 시간'),
        'endDate': openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_DATETIME, default=datetime.now().strftime('%Y-%m-%dT%H:%M'),description='종료 시간'),        
    }
)
update_calendar_params = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the event'),
            'color': openapi.Schema(type=openapi.TYPE_STRING, description='Color of the event'),
            'eventId': openapi.Schema(type=openapi.TYPE_STRING, description='Event ID'),
            'startDate': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,default=datetime.now().strftime('%Y-%m-%dT%H:%M'), description='Start date of the event (FORMAT_DATE: ex)2024-01-27T12:30)'),
            'endDate': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,default=datetime.now().strftime('%Y-%m-%dT%H:%M'), description='End date of the event (FORMAT_DATE: ex)2024-01-27T16:30)')
        }
    )

## Calendar name
post_calendar_name_parmas = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'calendar_id': openapi.Schema(type=openapi.TYPE_STRING, description='이벤트 고유번호'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='이름'),
        'school_id': openapi.Schema(type=openapi.TYPE_STRING, description='학번'),
    }
)
update_calendar_name_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'eventId': openapi.Schema(type=openapi.TYPE_STRING, description='Event ID'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='일정에 참가하는 이름'),
        'school_id': openapi.Schema(type=openapi.TYPE_STRING, description='school id'),
        'state_point': openapi.Schema(type=openapi.TYPE_INTEGER, description='출석 여부 point'),
        'state': openapi.Schema(type=openapi.TYPE_STRING, description='출석 상태'),
        'attendanceTime': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,default=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'), description='출석 시간'),
    }
)

## namelist
post_selslist_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='이름'),
        'is_admin': openapi.Schema(type=openapi.TYPE_STRING, description='직책', default='부원'),
        'sex': openapi.Schema(type=openapi.TYPE_STRING, description='성별'),
        'school_id': openapi.Schema(type=openapi.TYPE_STRING, description='학번'),
        'department': openapi.Schema(type=openapi.TYPE_STRING, description='학과',default='학과'),
        'attendance': openapi.Schema(type=openapi.TYPE_INTEGER, description='출석 횟수'),
        'accumulated_time': openapi.Schema(type=openapi.TYPE_INTEGER, description='누적 봉사시간'),
        'accumulated_cost': openapi.Schema(type=openapi.TYPE_INTEGER, description='누적 지각비'),
        'latencyCost': openapi.Schema(type=openapi.TYPE_INTEGER, description='현재 지각비'),
    }
)

post_reference_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(
            type=openapi.TYPE_STRING,
              description='게시물 제목'
              ),
        'upload_date': openapi.Schema(
            type=openapi.TYPE_STRING, 
            format=openapi.FORMAT_DATETIME, 
            description='생성 날짜', default=datetime.now().strftime('%Y-%m-%dT%H:%M')
            ),
        'content': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='내용'
            ),
    }
)

update_reference_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='게시물 번호',
        ),
        'title': openapi.Schema(
            type=openapi.TYPE_STRING,
              description='게시물 제목'
              ),
        'upload_date': openapi.Schema(
            type=openapi.TYPE_STRING, 
            format=openapi.FORMAT_DATETIME, 
            description='생성 날짜', default=datetime.now().strftime('%Y-%m-%dT%H:%M')
            ),
        'content': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='내용'
            ),
    }
)