from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Homework, SubmitHomework, HomeworkFile, SubmitHomeworkFile
from classroom.models import Classroom
from .serializers import HomeworkSerializer, HomeworkListSerializer, SubmitHomeworkSerializer, SubmitHomeworkListSerializer
from notice.serializers import NotificationSerializer
from django.db.models import Q

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import boto3
from datetime import datetime
from SHS.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# image
s3_client = boto3.client(
    's3',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

# 전체 숙제 조회 / (선생님) 새로운 숙제 생성
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def homework_list(request):
    classroom_id = int(request.user.classroom.id)
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    if request.method == 'GET':
        homeworks = Homework.objects.filter(classroom=classroom).order_by('-pk')
        serializer = HomeworkListSerializer(homeworks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            homework = serializer.save(classroom=classroom)

            # image_list = request.FILES.getlist('image_path')
            # for image in image_list:
            #     # item = HomeworkFile.objects.create(homework=homework, image=image)
            #     # item.save()
                
                    
            # 사진파일까지 저장되도록 한 번 더 저장
            # serializer.save()

            # 해당 반의 학생들 명단
            students = get_user_model().objects.filter(Q(classroom=classroom) & Q(usertype=2))

            data = {
                'classroom': classroom.id,
                'content': '숙제(' + request.data.get('title') + ')이 추가되었습니다.',
            }

            # 각 학생들마다 notification 추가해줌
            for student in students:
                notify = NotificationSerializer(data=data)
                if notify.is_valid(raise_exception=True):
                    notify.save(student=student)
                    # 알림 받은 학생의 is_notification값은 True로 바꿔주기
                    student.info.is_notification = True
                    student.info.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)




# 숙제 파일 저장
@api_view(['POST'])
def homeworkfile(request, homework_id):
    homework = get_object_or_404(Homework, pk=homework_id)

    # images = request.data
    
    for image in request.FILES.getlist('files'):
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
        HomeworkFile.objects.create(homework=homework, image=image_url)
   
    return Response(status=status.HTTP_201_CREATED)


# 숙제 상세 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE', 'POST',])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def homework_detail(request, homework_id):
    homework = get_object_or_404(Homework, pk=homework_id)

    if request.method == 'GET':
        serializer = HomeworkListSerializer(homework)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HomeworkSerializer(homework, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        homework.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        serializer = SubmitHomeworkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(student=request.user, homework=homework)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 제출한 파일 저장
@api_view(['POST',])
def submithomeworkfile(request, submithomework_id):
    submithomework = get_object_or_404(SubmitHomework, pk=submithomework_id)

    for image in request.FILES.getlist('files'):
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
        SubmitHomeworkFile.objects.create(image=image_url, submithomework=submithomework)

    return Response(status=status.HTTP_201_CREATED)


# 제출한 숙제 상세 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def submit_detail(request, submithomework_id):
    submit = get_object_or_404(SubmitHomework, pk=submithomework_id)
    if request.method == 'GET':
        serializer = SubmitHomeworkListSerializer(submit)    
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubmitHomeworkSerializer(submit, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        submit.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# (학생 기준) 제출한 숙제 목록 조회
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def submit(request):
    submits = get_list_or_404(SubmitHomework, student=request.user)
    serializer = SubmitHomeworkListSerializer(submits, many=True)
    return Response(serializer.data)