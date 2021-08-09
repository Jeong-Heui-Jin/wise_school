from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notice, NoticeFile, Notification
from .serializers import NoticeSerializer, NoticeListSerializer, NotificationSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# 해당 반의 공지사항 목록 조회 / 새 공지사항 작성
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def notice(request):
    classroom = request.user.classroom
    if request.method == 'GET':
        notices = get_list_or_404(Notice, classroom=classroom)
        serializer = NoticeListSerializer(notices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(classroom=classroom, teacher=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 해당 공지사항 상세 보기
@api_view(['GET', 'PUT', 'DELETE',])
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method == 'GET':
        serializer = NoticeSerializer(notice)    
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
@api_view(['GET', 'POST', 'DELETE',])
def notification(request, user_id):
    if request.method == 'GET':
        notifications = get_list_or_404(Notification, student=user_id)
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
def notification_detail(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    if request.method == 'GET':
        serializer = NotificationSerializer(notification)    
        return Response(serializer.data)

    elif request.method == 'DELETE':
        notification.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)