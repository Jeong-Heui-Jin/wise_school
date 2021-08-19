from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from student_manage.models import Note, Attendance, AttendanceChange
from .serializers import NoteSerializer, NoteListSerializer, AttendanceSerializer, AttendanceListSerializer, AttendanceChangeSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# 해당 반의 전체 출석 목록 조회 / 출석 입력
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def attendance(request):
    classroom = request.user.classroom
    if request.method == 'GET':
        attendances = get_list_or_404(Attendance, classroom=classroom)
        serializer = AttendanceListSerializer(attendances, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 각각의 학생이 요청 보냄.
            serializer.save(classroom=classroom, student=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 출석 상세 보기 & 출석 상태 변경 / 상태 변경 요청 제출
@api_view(['GET', 'PUT', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def attendance_detail(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'GET':
        serializer = AttendanceListSerializer(attendance)    
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AttendanceChangeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(attendance=attendance)
            return Response(serializer.data)


# 출석 상태 변경 요청 상세 조회 / 수정
@api_view(['GET', 'PUT',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def attendance_change(request, attendancechange_id):
    change = get_object_or_404(AttendanceChange, pk=attendancechange_id)

    if request.method == 'GET':
        serializer = AttendanceChangeSerializer(change)    
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AttendanceChangeSerializer(change, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 해당 학생의 태도 목록 조회 / 새로운 글 작성
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def note(request, student_id):
    student = get_object_or_404(get_user_model(), pk=student_id)
    if request.method == 'GET':
        notes = Note.objects.filter(student=student)
        serializer = NoteListSerializer(notes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(teacher=request.user, student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 학생 태도 상세 보기
@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'GET':
        serializer = NoteListSerializer(note)
        return Response(serializer.data)
    else:
        # 현재 사용자와 작성자가 일치하지 않을 경우 수정/삭제하지 못함.
        if not request.user.wrote_notes.filter(pk=note_id).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            if request.method == 'PUT':
                serializer = NoteSerializer(note, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
            elif request.method == 'DELETE':
                note.delete()
                data = {
                    'delete': '삭제되었습니다.'
                }
                return Response(data, status=status.HTTP_204_NO_CONTENT)