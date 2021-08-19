from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer, MessageListSerializer
from django.db.models import Q
from itertools import chain
from django.contrib.auth import get_user_model

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# 해당 학생의 전체 메시지 목록 조회 (+ 시간 순서대로 최근꺼를 맨 위로 / 안 읽은 갯수 표시)
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def message_list(request):
    # user = get_object_or_404(get_user_model(), pk=request.user.id)
    # 해당 학생과 대화한 상대 모두 가져오기
    senders = Message.objects.filter(receiver=request.user).values_list('sender', flat=True).distinct()
    receivers = Message.objects.filter(sender=request.user).values_list('receiver', flat=True).distinct()
    # 두 명단 합치기
    buddies = list(set(list(chain(senders, receivers))))
    # buddies = list(chain(senders, receivers)).remove(request.user)

    # 각 대화상대마다, 안읽은갯수+가장최근대화 묶어서 딕셔너리 형태로 저장한 것들을 리스트에 넣어줌.
    messages_list = []
    for buddy in buddies:
        # 그 상대와 나눈 대화 전부 가져오기
        messages = Message.objects.filter((Q(receiver=request.user)&Q(sender=buddy))|(Q(receiver=buddy)&Q(sender=request.user))).order_by('-sendtime')
        # 그 중 읽지 않은 메시지 갯수
        unread_cnt = messages.filter(Q(is_checked=False)&Q(sender=buddy)).count()
        # 그 중 가장 최근 메시지
        latest = MessageListSerializer(messages, many=True).data[0]
        # 그 대화 상대와의 대화 정보 담은 딕셔너리를 messages_list 리스트에 차례대로 넣어줌.
        chat_info = {
            'latest': latest,
            'unread_cnt' : unread_cnt,
        }
        messages_list.append(chat_info)
    
    messages = {
        'messages': sorted(messages_list, key=lambda x:x.get('latest').get('sendtime'), reverse=True),
    }
    return JsonResponse(messages)


# 특정 상대화의 대화 내용 모두 가져오기 / 새로운 메시지 작성
# is_checked가 False인 객체들 전부 True로 바꿔주기
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def talk(request, buddy_id):
    buddy = get_object_or_404(get_user_model(), pk=buddy_id)
    if request.method == 'GET':
        # 해당 상대와 나눈 대화 모두 가져오기
        messages = Message.objects.filter((Q(receiver=request.user)&Q(sender=buddy))|(Q(receiver=buddy)&Q(sender=request.user))).order_by('-sendtime')
        
        # 해당 상대와의 메시지 중 내가 받은 메시지이며 is_checked값이 False인 것들을 전부 True로 바꿔줌
        for message in messages.filter(Q(receiver=request.user)&Q(is_checked=False)):
            message.is_checked = True
            message.save()
        
        # 해당 사용자가 받은 메시지를 모두 확인했다면 is_message값 false로 바꿔주기
        if not Message.objects.filter(Q(receiver=request.user)&Q(is_checked=False)).exists():
            request.user.is_message = False
            request.user.save()
        
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(sender=request.user, receiver=buddy, is_checked=False)

            buddy.is_message = True
            buddy.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)