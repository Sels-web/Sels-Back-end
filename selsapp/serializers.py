from rest_framework.serializers import ModelSerializer
from .models import Selslist,Calendar

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = Selslist
        fields = '__all__'

class CalendarDataSerializer(ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'