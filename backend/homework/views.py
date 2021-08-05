from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Homework, SubmitHomework
from .serializers import HomeworkSerializer, SubmitHomeworkSerializer
from homework import serializers



# 전체 숙제 조회 / (선생님) 새로운 숙제 생성
@api_view(['GET', 'POST',])
def homework_list(request):
    user = request.user
    class_id = user.classroom.id

    if request.method == 'GET':
        homeworks = get_list_or_404(Homework, classroom=class_id)
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(classroom=class_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 숙제 상세 보기
@api_view(['GET',])
def homework_detail(request, homework_id):
    homework = get_object_or_404(Homework, pk=homework_id)
    serializer = HomeworkSerializer(homework)
    return Response(serializer.data)


# 제출한 숙제 상세 보기
@api_view(['GET', 'PUT', 'DELETE',])
def submit_detail(request, submithomework_id):
    submit = get_object_or_404(SubmitHomework, pk=submithomework_id)
    if request.method == 'GET':
        serializer = SubmitHomeworkSerializer(submit)    
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubmitHomeworkSerializer(submit, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        submit.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# (학생 기준) 제출한 숙제 목록 조회 / 새로운 숙제 제출
@api_view(['GET', 'POST',])
def submit_list(request):
    if request.method == 'GET':
        submits = get_list_or_404(SubmitHomework, user=request.user)
        serializer = SubmitHomeworkSerializer(submits, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubmitHomeworkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)