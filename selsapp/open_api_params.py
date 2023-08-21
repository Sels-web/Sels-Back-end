from drf_yasg import openapi
from .models import *

# ## 캘린더 일정 등록
# # input: JSON(title, startDate, endDate, Color, evnetId)
# # output: x
post_calendar_params = [
    openapi.Parameter(
        "title",
        openapi.IN_QUERY,
        description="Title of the event",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "Color",
        openapi.IN_QUERY,
        description="Color of the event",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "eventId",
        openapi.IN_QUERY,
        description="Event ID",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "startDate",
        openapi.IN_QUERY,
        description="Start date of the event (FORMAT_DATE: ex)2024-01-27T12:30)",
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME,
        default = '2024-01-27T12:30'
    ),
    openapi.Parameter(
        "endDate",
        openapi.IN_QUERY,
        description="End date of the event (FORMAT_DATE: ex)2024-01-27T16:30)",
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME,
        default = '2024-01-27T15:30'
    ),
]
update_calendar_params = [
    openapi.Parameter(
        "title",
        openapi.IN_QUERY,
        description="Title of the event",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "Color",
        openapi.IN_QUERY,
        description="Color of the event",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "eventId",
        openapi.IN_QUERY,
        description="Event ID",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "startDate",
        openapi.IN_QUERY,
        description="Start date of the event (FORMAT_DATE: ex)2024-01-27T12:30)",
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME,
        default = '2024-01-27T12:30'
    ),
    openapi.Parameter(
        "endDate",
        openapi.IN_QUERY,
        description="End date of the event (FORMAT_DATE: ex)2024-01-27T16:30)",
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME,
        default = '2024-01-27T15:30'
    ),
]
post_calendar_name_parmas = [
    openapi.Parameter(
        "eventId",
        openapi.IN_QUERY,
        description="Event ID",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "name",
        openapi.IN_QUERY,
        description="일정에 참가하는 이름",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "school_id",
        openapi.IN_QUERY,
        description="school id",
        type=openapi.TYPE_STRING
    ),
]
post_selslist_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'school_id': openapi.Schema(type=openapi.TYPE_STRING, description='학번'),
        'sex': openapi.Schema(type=openapi.TYPE_STRING, description='성별'),
        'department': openapi.Schema(type=openapi.TYPE_STRING, description='학과'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='이름'),
        'is_admin': openapi.Schema(type=openapi.TYPE_STRING, description='직책'),
        'attendance': openapi.Schema(type=openapi.TYPE_INTEGER, description='출석 횟수'),
        'accumulated_time': openapi.Schema(type=openapi.TYPE_INTEGER, description='누적 봉사시간'),
        'accumulated_cost': openapi.Schema(type=openapi.TYPE_INTEGER, description='누적 지각비'),
        'latencyCost': openapi.Schema(type=openapi.TYPE_INTEGER, description='현재 지각비'),
    }
)
update_calendar_name_parmas = [
    openapi.Parameter(
        "eventId",
        openapi.IN_QUERY,
        description="Event ID",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "name",
        openapi.IN_QUERY,
        description="일정에 참가하는 이름",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "school_id",
        openapi.IN_QUERY,
        description="school id",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "state_point",
        openapi.IN_QUERY,
        description="출석 여부 point",
        type=openapi.TYPE_INTEGER
    ),
    openapi.Parameter(
        "state",
        openapi.IN_QUERY,
        description="출석 상태",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "attendanceTime",
        openapi.IN_QUERY,
        description="출석 시간",
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME
    ),
    
]