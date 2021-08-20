from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notice, NoticeFile, Notification
from .serializers import NoticeSerializer, NoticeListSerializer, NotificationSerializer
from django.db.models import Q

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from datetime import datetime
import boto3
from SHS.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# image
s3_client = boto3.client(
    's3',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

# 해당 반의 공지사항 목록 조회 / 새 공지사항 작성
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def notice(request):
    classroom = request.user.classroom

    # classroom = request.user.classroom
    if request.method == 'GET':
        notices = Notice.objects.filter(classroom=classroom)
        serializer = NoticeListSerializer(notices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(classroom=classroom, teacher=request.user)

            # 해당 반의 학생들 명단
            students = get_user_model().objects.filter(Q(classroom=classroom) & Q(usertype=2))

            data = {
                'classroom': classroom.id,
                'content': '공지사항(' + request.data.get('title') + ')이 추가되었습니다.',
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


# 공지 파일 저장
@api_view(['POST',])
def noticefile(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)

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
        NoticeFile.objects.create(image=image_url, notice=notice)
   
    return Response(status=status.HTTP_201_CREATED)


# 해당 공지사항 상세 보기
@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method == 'GET':
        serializer = NoticeListSerializer(notice)    
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        notice.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 해당 학생의 알림 목록 조회 / 새 알림 생성 / 해당 학생의 알림 전체 삭제
# 알림 목록 조회시 해당 학생의 is_notification값 False로 바꿔주기
@api_view(['GET', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def notification(request, user_id):
    if request.method == 'GET':
        notifications = get_list_or_404(Notification, student=user_id)
        user = request.user
        user.info.is_notification = False
        user.info.save()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        Notification.objects.filter(student=user_id).delete()
        data = {
            'delete': '알림이 모두 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 알림 상세 보기
@api_view(['GET', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def notification_detail(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    if request.method == 'GET':
        serializer = NotificationSerializer(notification)    
        return Response(serializer.data)

    elif request.method == 'DELETE':
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)