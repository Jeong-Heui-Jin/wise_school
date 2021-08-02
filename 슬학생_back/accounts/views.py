from django.db.models import manager
from accounts.models import Parents
from django.shortcuts import get_object_or_404, render, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParentSerializer, ParentsListSerializer, UserSerializer, UserListSerializer, ServiceRequestSerializer
from accounts import serializers ParentsListSerializer
from django.contrib.auth import get_user_model
from rest_auth.views import PasswordResetView
from django.conntrib.auth.forms import SetPasswordForm


# class CustomPasswordResetView(PasswordResetView):
#     pass


# 신규 서비스 신청
@api_view(['POST',])
def service_request(request):
    serializer = ServiceRequestSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def password_reset(request):
    # if passwordForm.is_valid():
    #     password = passwordForm.cleaned_data['password']
    #     request.user.password = make_password(password)
    #     request.user.save()
    # SetPasswordForm
    pass


# 해당 사용자의 정보 조회/수정/삭제
def info(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    # serializer = UserSerializer(user)
    # return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 해당 학생의 보호자들 목록 조회
def parents(request, user_id):
    parents_list = get_list_or_404(Parents, pk=user_id)
    serializer = ParentsListSerializer(parents_list, many=True)
    return Response(serializer.data)


# 해당 학교의 선생님들 목록 조회
def teachers(request, school_id):
    teachers_list = get_list_or_404(Parents, classroom_school_id=school_id)
    serializer = UserListSerializer(teachers_list, many=True)
    return Response(serializer.data)


# 해당 학교의 학생들 목록 조회
def students(request, school_id):
    students_list = get_list_or_404(get_user_model(), classroom_school_id=school_id)
    serializer = UserListSerializer(students_list, many=True)
    return Response(serializer.data)


# 해당 학생의 상세 정보 조회
# def student(request, user_id):
#     student = get_object_or_404(get_user_model(), pk=user_id)
#     serializer = UserSerializer(student)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_student(request):
# 	#1-1. Client에서 온 데이터를 받아서
#     password = request.data.get('password')
#     password_confirmation = request.data.get('passwordConfirmation')
		
# 	#1-2. 패스워드 일치 여부 체크
#     if password != password_confirmation:
#         return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
# 	#2. UserSerializer를 통해 데이터 직렬화
#     serializer = UserSerializer(data=request.data)
    
# 	#3. validation 작업 진행 -> password도 같이 직렬화 진행
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.save()
#         #4. 비밀번호 해싱 후 
#         user.set_password(request.data.get('password'))
#         user.save()
#         # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
#         return Response(serializer.data, status=status.HTTP_201_CREATED)