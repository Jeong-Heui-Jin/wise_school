from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from accounts.serializers import UserListSerializer
from .serializers import TimetableSerializer, TimetableDetailSerializer
from django.contrib.auth import get_user_model
from .models import Timetable, TimetableDetail


# 반 친구들 + 선생님 목록 조회
@api_view(['GET',])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def members(request, class_id):
    class_members = get_list_or_404(get_user_model(), class_id=class_id)
    serializer = UserListSerializer(class_members, many=True)
    return Response(serializer.data)


# 전체 시간표 생성
@api_view(['POST',])
def timetable_create(request, class_id):
    serializer = TimetableSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(classroom=class_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 전체 시간표 조회 / 시간표 상세 생성
@api_view(['GET', 'POST',])
def timetable(request, timetable_id):
    if request.method == 'GET':
        timetable = get_object_or_404(Timetable, pk=timetable_id)
        serializer = TimetableSerializer(timetable)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TimetableDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(timetable=timetable_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 시간표 상세 수정/삭제
@api_view(['PUT', 'DELETE',])
def timetable_detail(request, timetabledetail_id):
    detail = get_object_or_404(TimetableDetail, pk=timetabledetail_id)

    if request.method == 'PUT':
        serializer = TimetableDetailSerializer(detail, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        detail.delete()
        return Response({ 'id': timetabledetail_id }, status=status.HTTP_204_NO_CONTENT)