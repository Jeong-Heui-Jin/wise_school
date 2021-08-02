from .models import Parents, StudentInfo, ServiceRequest
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentInfo
        fields = '__all__'
        read_only_rields = ('user',)


class ParentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = '__all__'
        read_only_rields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # 아래꺼에 write_only 넣어줘야되나?
    student_infos = StudentInfoSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'usertype', 'phone', 'is_message', 'student_infos',)