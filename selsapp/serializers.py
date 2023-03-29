from rest_framework.serializers import ModelSerializer
from .models import Selslist

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = Selslist
        fields = '__all__'