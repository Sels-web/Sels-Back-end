from drf_yasg import openapi

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
post_params = [
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