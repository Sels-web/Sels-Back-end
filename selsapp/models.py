# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.utils import timezone

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Selslist(models.Model):
    school_id = models.CharField(max_length=500, default='') # 학번
    sex = models.CharField(max_length=50, default='')
    department = models.CharField(max_length=500, default='') # 전공
    name = models.CharField(max_length=500) # 이름
    is_admin = models.CharField(max_length=500, null=True) # 직책
    
    attendance = models.IntegerField(default=0) # 출석횟수
    accumulated_time = models.IntegerField(default=0) # 누적 봉사시간
    accumulated_cost = models.IntegerField(default=0) # 누적 지각비
    latencyCost = models.IntegerField(default=0) # 정산해야하는 지각비
    penalty_cnt = models.IntegerField(default=0) # 경고 횟수

    class Meta:
        db_table = 'Selslist'

class Calendar(models.Model):
    title = models.CharField(max_length=500)
    startDate = models.DateTimeField(default=timezone.now)
    endDate = models.DateTimeField(default=timezone.now)
    color = models.CharField(max_length=100)
    eventId = models.CharField(max_length=100,default='')
    activity_time = models.IntegerField(default=0)

    class Meta:
        db_table = 'Calendar'
        managed=True

class Calendar_NameList(models.Model):
    # 필요한 parameter
    calendar_id = models.CharField(max_length=100, default='')
    school_id = models.CharField(max_length=500, default='')
    name = models.CharField(max_length=500)
    attendanceTime = models.DateTimeField(default=timezone.now) 

    # 계산되어 저장되는 값
    state = models.IntegerField(default=0) # 0: default 1: 참석 2: 1-10분 지각 3: 11분 이상 지각 4: 노쇼
    late_time = models.CharField(max_length=500,default='')
    latency_cost = models.IntegerField(default=0)
    service_time = models.IntegerField(default=0)
    penalty = models.IntegerField(default=0)

    # 정산함수에서 필요
    calculated = models.IntegerField(default=0)

    class Meta:
        db_table = 'Calendar_NameList'
        managed = True

class Reference(models.Model):
    title = models.CharField(max_length = 1000)
    upload_date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length = 5000, default='')

    class Meta:
        db_table = 'Reference'
        managed = True

class File_TB(models.Model):
    reference_id = models.IntegerField()
    file_location = models.FileField(upload_to='Uploaded Files/%y/%m/%d/', blank=True)

    class Meta:
        db_table = 'File_TB'
        managed = True
