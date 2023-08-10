from drf_yasg import openapi
from .models import *
get_params = [
	openapi.Parameter(
        "start_date",
        openapi.IN_QUERY,
        description="yyyy-mm-dd",
        type=openapi.FORMAT_DATE,
        default=""
    ),
    openapi.Parameter(
        "end_date",
        openapi.IN_QUERY,
        description="yyyy-mm-dd",
        type=openapi.FORMAT_DATE,
        default=""
    )
]
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
        format=openapi.FORMAT_DATETIME
    ),
    openapi.Parameter(
        "endDate",
        openapi.IN_QUERY,
        description="End date of the event (FORMAT_DATE: ex)2024-01-27T16:30)",
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME
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
        format=openapi.FORMAT_DATETIME
    ),
    openapi.Parameter(
        "endDate",
        openapi.IN_QUERY,
        description="End date of the event (FORMAT_DATE: ex)2024-01-27T16:30)",
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME
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
post_selslist_params = [
    openapi.Parameter(
        "school_id",
        openapi.IN_QUERY,
        description="학번",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "sex",
        openapi.IN_QUERY,
        description="성별",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "department",
        openapi.IN_QUERY,
        description="학과",
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "name",
        openapi.IN_QUERY,
        description="이름",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "is_admin",
        openapi.IN_QUERY,
        description="직책",
        type=openapi.TYPE_STRING,
        default='부원'
    ),
        openapi.Parameter(
        "attendance",
        openapi.IN_QUERY,
        description="참석 횟수",
        type=openapi.TYPE_INTEGER,
        default=0
    ),
        openapi.Parameter(
        "accumulated_time",
        openapi.IN_QUERY,
        description="누적 봉사시간",
        type=openapi.TYPE_INTEGER,
        default=0
    ),
        openapi.Parameter(
        "accumulated_cost",
        openapi.IN_QUERY,
        description="누적 지각비",
        type=openapi.TYPE_INTEGER,
        default=0
    ),
        openapi.Parameter(
        "latencyCost",
        openapi.IN_QUERY,
        description="현재 지각비",
        type=openapi.TYPE_INTEGER,
        default=0
    ),
]
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