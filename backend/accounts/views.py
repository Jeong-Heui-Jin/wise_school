from django.db.models import manager
from django.http.response import JsonResponse
from .models import User, Parents
from classroom.models import School, Classroom
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserImgSerializer, ParentSerializer, StudentInfoSerializer, UserSerializer, UserListSerializer, ServiceRequestSerializer, SignupSerializer, StudentInfoSerializer
from classroom.serializers import ClassroomSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import boto3
from datetime import datetime
from SHS.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

import random

# image
s3_client = boto3.client(
    's3',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

profile_images_paths = [
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:05:48.141002.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:04:02.205511.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:05:48.141002.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:10:19.594827.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:10:30.263697.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:10:40.844359.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:10:56.319531.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:11:16.984994.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:11:27.097556.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:11:57.902993.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:12:06.631970.png',
    'http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-1818:12:16.082815.png',
]



# 신규 서비스 신청
@api_view(['POST',])
def service_request(request):
    serializer = ServiceRequestSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 해당 정보가 전부 한 사용자를 가리키면, 그 사용자 객체를 넘겨줌.
@api_view(['POST',])
def user_confirm(request):
    username = request.data.get('username')
    user = get_object_or_404(User, username=username)
    if user.name == request.data.get('name') and user.phone == request.data.get('phone'):
        serializer = UserSerializer(user)
        return Response(serializer.data)
    # 일치하지 않을 경우 에러 발생
    return Response({'error': '사용자 정보가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 비밀번호 재설정
@api_view(['POST',])
def password_reset(request):
    username = request.data.get('username')
    new_password = request.data.get('password')
    # 일치 여부는 front에서 확인해서 넘겨주면 될 듯.
    # password_confirm = request.data.get('passwordConfirmation')

    user = get_object_or_404(get_user_model(), username=username)
    user.set_password(new_password)
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST', 'GET',])
def change_password(request):
    form = PasswordChangeForm(request.user, request.data)
    # old_password, new_password1, new_password2
    if form.is_valid():
        form.save()
        # 비밀번호 변경 후에도 로그인 유지할 수 있도록
        update_session_auth_hash(request, form.user)
        return Response({'success' : '비밀번호 변경 성공'})
    return Response({'error': '비밀번호가 올바르지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 현재 사용자의 정보 조회
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['PUT',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def image_change(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)

    # 프로필 image 파일
    image = request.FILES['files']
    image_time = (str(datetime.now())).replace(" ","") # 이미지이름을 시간으로 설정하기 위해 datetime를 사용했다.
    image_type = (image.content_type).split("/")[1]
    s3_client.upload_fileobj(
        image,
        "dycho96", # 버킷이름
        image_time+"."+image_type,
        ExtraArgs = {
            "ContentType" : image.content_type
        }
    )
    image_url = image_time+"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨
    image_url = image_url.replace(" ","/")

    print(image_url)

    data = {
        'image': image_url,
    }
    serializer = UserImgSerializer(user, data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(image=image_url)
        return Response(serializer.data)


# 해당 사용자의 정보 조회/수정/삭제
@api_view(['GET', 'PUT','DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def info(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        user_info = {
            'info': serializer.data,
            'class_num': user.classroom.grade,
        }
        return JsonResponse(user_info)

    elif request.method == 'PUT':
        # student.info 정보 수정
        info_data = {
            'number' : request.data.get('number'),
            'address' : request.data.get('address'),
            'is_notification' : user.is_notification,
        }
        serializer = StudentInfoSerializer(user.info, data=info_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        # 프로필 image 파일
        # image = request.FILES['files']
        # image_time = (str(datetime.now())).replace(" ","") # 이미지이름을 시간으로 설정하기 위해 datetime를 사용했다.
        # image_type = (image.content_type).split("/")[1]
        # s3_client.upload_fileobj(
        #     image,
        #     "dycho96", # 버킷이름
        #     image_time+"."+image_type,
        #     ExtraArgs = {
        #         "ContentType" : image.content_type
        #     }
        # )
        # image_url = "http://dycho96.s3.ap-northeast-2.amazonaws.com/"+image_time+"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨
        # image_url = image_url.replace(" ","/")
        
        # user 정보 수정
        user_data = {
            'name' : request.data.get('name'),
            'phone' : request.data.get('phone'),
            'classroom_id' : user.classroom.id,
            # 'image': image_url,
        }
        # print(user_data)
        serializer = UserListSerializer(user, data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 해당 학생의 보호자들 목록 조회 / 추가
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def parents_list(request, user_id):
    student = get_object_or_404(get_user_model(), pk=user_id)
    if request.method == 'GET':
        parents_list = Parents.objects.filter(pk=user_id)
        serializer = ParentSerializer(parents_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 보호자 상세 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE',])
def parent_detail(request, parent_id):
    parent = get_object_or_404(Parents, pk=parent_id)
    if request.method == 'GET':
        serializer = ParentSerializer(parent)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        parent.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 반 친구들 + 선생님 목록 조회
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def class_members(request):
    classroom = request.user.classroom
    class_members = get_list_or_404(User, classroom=classroom)
    members = UserSerializer(class_members, many=True).data

    teacher = [member for member in members if member.get('usertype')==1][0]
    students = [member for member in members if member.get('usertype')==2]

    class_info = {
        'teacher': teacher,
        'students': students,
        'classroom': ClassroomSerializer(classroom).data,
    }
    return JsonResponse(class_info)


# 해당 학교의 선생님들 목록 조회 (학교 관리자)
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def teachers(request):
    # 해당 사용자가 속한 학교
    school = request.user.classroom.school
    # 그 학교에 속한 선생님들(usertype=1인 user들) 목록
    teachers_list = get_user_model().objects.filter(classroom__school=school, usertype=1)
    serializer = UserSerializer(teachers_list, many=True)
    return Response(serializer.data)


# 해당 학교의 학생들 목록 조회 (학교 관리자)
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def students(request):
    # 해당 사용자가 속한 학교
    school = request.user.classroom.school
    # 그 학교에 속한 학생들(usertype=2인 user들) 목록
    students_list = get_user_model().objects.filter(classroom__school=school, usertype=2)
    serializer = UserSerializer(students_list, many=True)
    return Response(serializer.data)


# 학생 계정 생성
@api_view(['POST'])
def create_student(request, school_id):
    school = get_object_or_404(School, pk=school_id)

    students_num = int(request.data.get('students_num'))
    i = 0
    for _ in range(students_num):
        user = User(id=i, usertype=2, classroom_school_id=school)
        user.save()
        i += 1

    teachers_num = int(request.data.get('teachers_num'))
    for _ in range(teachers_num):
        user = User(id=i, usertype=1, classroom_school=school)
        user.save()
        i += 1

    return Response({'created':'계정이 생성되었습니다.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def signup(request):
    print('1234')
    password = request.data.get('password')
    class_id = request.data.get('class_id')
    room = get_object_or_404(Classroom, pk=class_id)

    serializer = SignupSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        
        user.set_password(password)
        user.classroom = room
        random_num = random.randint(0, 11)
        user.image = profile_images_paths[random_num]
        user.save()

        if user.usertype == 2:
            info = StudentInfoSerializer(data={})
            if info.is_valid(raise_exception=True):
                info.save(student=user)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)