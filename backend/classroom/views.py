from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from homework.serializers import HomeworkSerializer
from homework.models import Homework
from notice.serializers import NoticeListSerializer
from notice.models import Notice
from .serializers import TimetableSerializer, TimetableListSerializer, TimetableDetailSerializer
from .models import Timetable, TimetableDetail



# 전체 시간표 생성
@api_view(['POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def timetable_create(request):
    classroom = request.user.classroom
    serializer = TimetableSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(classroom=classroom)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 전체 시간표 조회 / 시간표 상세 생성
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def timetable(request):
    user = request.user
    timetable = get_object_or_404(Timetable, classroom=user.classroom)
    if request.method == 'GET':
        timetable = get_object_or_404(Timetable, pk=timetable.id)
        serializer = TimetableListSerializer(timetable)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TimetableDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(timetable=timetable)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 시간표 상세 수정/삭제
@api_view(['PUT', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def timetable_detail(request, timetabledetail_id):
    detail = get_object_or_404(TimetableDetail, pk=timetabledetail_id)

    if request.method == 'PUT':
        serializer = TimetableDetailSerializer(detail, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        detail.delete()
        return Response({ 'deleted': timetabledetail_id }, status=status.HTTP_204_NO_CONTENT)


# 전체 시간표 조회 / 시간표 상세 생성
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    classroom = request.user.classroom

    homeworks = HomeworkSerializer(get_list_or_404(Homework, classroom=classroom), many=True)
    timetable = TimetableListSerializer(get_object_or_404(Timetable, classroom=classroom))
    notices = NoticeListSerializer(get_list_or_404(Notice, classroom=classroom), many=True)

    data = {
        'homeworks': homeworks.data[:-6:-1],
        'notices': notices.data[:-6:-1],
        'timetable': timetable.data,
    }
    return JsonResponse(data)