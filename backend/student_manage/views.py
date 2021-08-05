from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from student_manage.models import Note, Attendance, AttendanceChange
from .serializers import NoteSerializer, AttendanceSerializer, AttendanceChangeSerializer
from homework import serializers



# 해당 반의 전체 출석 목록 조회 / 출석 입력
@api_view(['GET', 'POST',])
def attendance_list(request, class_id):
    if request.method == 'GET':
        attendances = get_list_or_404(Attendance, classroom=class_id)
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(classroom=class_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 출석 상세 보기 / 출석 상태 변경
@api_view(['GET', 'PUT',])
def attendance_detail(request, student_id, date):
    attendance = get_object_or_404(Attendance, student=student_id, date=date)
    if request.method == 'GET':
        serializer = AttendanceSerializer(attendance)    
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 출석 상태 변경 요청 제출
@api_view(['PUT',])
def attendance_change(request, student_id, date):
    change = get_object_or_404(AttendanceChange, student=student_id, date=date)
    serializer = AttendanceChangeSerializer(change, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


# 해당 학생의 태도 목록 조회 / 새로운 글 작성
@api_view(['GET', 'POST',])
def note_list(request, student_id):
    if request.method == 'GET':
        notes = get_list_or_404(Note, student=student_id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(teacher=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 학생 태도 상세 보기
@api_view(['GET', 'PUT', 'DELETE',])
def note_detail(request, student_id, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'GET':
        serializer = NoteSerializer(note)    
        return Response(serializer.data)
    else:
        # 현재 사용자와 작성자가 일치하지 않을 경우 수정/삭제하지 못함.
        if not request.user.note_set.filter(pk=note_id).exists():
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