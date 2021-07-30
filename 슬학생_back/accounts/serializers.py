from accounts.views import parents
from accounts.models import Parents, StudentInfo
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentInfo
        fields = '__all__'
        read_only_rields = ('user',)


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = '__all__'
        read_only_rields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    student_infos = StudentInfoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'usertype', 'phone', 'is_Message', 'student_infos',)


# 전체 학생/선생님 명단
class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



# class CustomTokenSerializer(serializers.Serializer):
#     token = serializers.CharField()