from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notice, NoticeFile, Notification
from .serializers import NoticeSerializer, NoticeFileSerializer, NotificationSerializer
from homework import serializers



# 해당 반의 공지사항 목록 조회 / 새 공지사항 작성
@api_view(['GET', 'POST',])
def notice_list(request, class_id):
    if request.method == 'GET':
        notices = get_list_or_404(Notice, classroom=class_id)
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(classroom=class_id)
            # 공지사항 추가되자마자 반의 모든 학생들에게 자동으로 알림 object 추가되도록 하기.
            # 학생 명단 받아서 for문으로 일일이 넣어줘야되나...?
            # 아니면 그냥 알림 생성되는 함수를 따로 만드는게 나은가...
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
# 알림 : 숙제 / 공지사항 추가 (+ 수업 시작)
@api_view(['GET', 'POST', 'DELETE',])
def notification_list(request, user_id):
    if request.method == 'GET':
        notifications = get_list_or_404(Notification, student=user_id)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = NotificationSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(teacher=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
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