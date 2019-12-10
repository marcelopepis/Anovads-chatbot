from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from core.models import Log

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class LogSerializer(ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'