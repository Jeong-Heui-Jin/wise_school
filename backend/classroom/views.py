from django.contrib.auth import get_user_model
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


# 전체 시간표 조회/수정 / 시간표 상세 생성
@api_view(['GET', 'POST', 'PUT',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def timetable(request):

    if request.method == 'GET':
        if Timetable.objects.filter(classroom=request.user.classroom):
            timetable = TimetableListSerializer(get_object_or_404(Timetable, classroom=request.user.classroom))
            return Response(timetable.data)
        else:
            timetable = {}
            return Response(timetable)
    
    elif request.method == 'POST':
        timetable = get_object_or_404(Timetable, classroom=request.user.classroom)
        serializer = TimetableDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(timetable=timetable)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        timetable = get_object_or_404(Timetable, classroom=request.user.classroom)
        serializer = TimetableSerializer(timetable, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
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


# 홈 페이지에 들어갈 정보들
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    classroom = request.user.classroom
    # user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    # classroom = user.classroom

    if Homework.objects.filter(classroom=classroom):
        homeworks = HomeworkSerializer(get_list_or_404(Homework, classroom=classroom), many=True)
    else:
        homeworks = []

    if Timetable.objects.filter(classroom=classroom):
        timetable = TimetableListSerializer(get_object_or_404(Timetable, classroom=classroom)).data
        details = {
            'mon': [],
            'tue': [],
            'wed': [],
            'thu': [],
            'fri': [],
        }
        for detail in timetable.get('details'):
            for day in list(details.keys()):
                details[day].append({'subject':detail[day], 'time':detail['start'][:5]+' ~ '+detail['end'][:5]})
        # timetable.update({'days':details})
        timetable['details'] = details
    else:
        timetable = {}

    if Notice.objects.filter(classroom=classroom):
        notices = NoticeListSerializer(get_list_or_404(Notice, classroom=classroom), many=True)
    else:
        notices = []

    data = {
        'homeworks': homeworks.data[:-6:-1],
        'notices': notices.data[:-6:-1],
        'timetable': timetable,
    }
    return JsonResponse(data)