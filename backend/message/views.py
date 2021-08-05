from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer
from django.db.models import Q
from itertools import chain
from django.contrib.auth import get_user_model



# 해당 학생의 전체 메시지 목록 조회 (+ 시간 순서대로 최근꺼를 맨 위로 / 안 읽은 갯수 표시)
# 해당 사용자의 is_message값 true로 바꿔주기
@api_view(['GET',])
def message_list(request, receiver_id):
    # 해당 사용자의 is_message값 true로 바꿔주기
    user = get_object_or_404(get_user_model(), pk=receiver_id)
    user.is_message = True
    user.save()

    # 해당 학생과 대화한 상대 모두 가져오기
    senders = Message.objects.filter(receiver=receiver_id).dinstinct('sender')
    receivers = Message.objects.filter(sender=receiver_id).dinstinct('receiver')
    # 리스트에서 해당 학생은 빼기
    buddies = list(chain(senders, receivers)).remove(request.user.id)

    # 각 대화상대마다, 안읽은갯수+가장최근대화 묶어서 딕셔너리 형태로 저장한 것들을 리스트에 넣어줌.
    messages_list = []
    for buddy in buddies:
        # 그 상대와 나눈 대화 전부 가져오기
        messages = Message.objects.filter(Q(receiver=buddy)|Q(sender=buddy)).order_by('-sendtime')
        # 그 중 읽지 않은 메시지 갯수
        unread_cnt = messages.filter(is_checked=False).count()
        # 그 중 가장 최근 메시지
        latest = messages[0]
        # 그 대화 상대와의 대화 정보 담은 딕셔너리를 messages_list 리스트에 차례대로 넣어줌.
        chat_info = {
            'latest': latest,
            'unread_cnt' : unread_cnt,
        }
        messages_list.append(chat_info)

    return JsonResponse(messages_list)


# 특정 상대화의 대화 내용 모두 가져오기 / 새로운 메시지 작성
# is_checked가 False인 객체들 전부 True로 바꿔주기
@api_view(['GET', 'POST',])
def talk(request, sender_id, receiver_id):
    if request.method == 'GET':
        messages = Message.objects.filter((Q(receiver=receiver_id)&Q(sender=sender_id))|(Q(receiver=sender_id)&Q(sender=receiver_id))).order_by('-sendtime')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(sender=request.user.id, receiver=sender_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)