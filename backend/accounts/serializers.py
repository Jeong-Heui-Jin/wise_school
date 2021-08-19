from .models import Parents, StudentInfo, ServiceRequest
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentInfo
        # student값 자체가 pk값이므로 id 안 가져옴.
        fields = ('number', 'address', 'is_notification',)
        read_only_fields = ('student',)


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = ('id', 'name', 'phone', 'relation',)
        read_only_fields = ('student',)


# 선생님/학생 정보 불러올 때 사용
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    info = StudentInfoSerializer()
    parents = ParentSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'classroom', 'username', 'password', 'name', 'usertype', 'phone', 'is_message', 'image', 'info', 'parents',)


# 관리자 페이지에서 선생님/학생 목록 불러올 때 사용
class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'classroom', 'name', 'phone',)
        # read_only_fields = ('image',)
        # fields = '__all__'

# 사용자 프로필 이미지 변경
class UserImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('image',)
        read_only_fields = ('image',)
        # fields = '__all__'


# class UserImageChangeSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('image',)
#         # read_only_fields = ('image',)


class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceRequest
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'usertype',)
        read_only_fields = ('classroom',)