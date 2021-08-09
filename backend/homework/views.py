from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Homework, SubmitHomework
from classroom.models import Classroom
from .serializers import HomeworkSerializer, SubmitHomeworkSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# 전체 숙제 조회 / (선생님) 새로운 숙제 생성
@api_view(['GET', 'POST',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def homework_list(request):
    classroom_id = int(request.user.classroom.id)
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    if request.method == 'GET':
        homeworks = get_list_or_404(Homework, classroom=classroom)[::-1]
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(classroom=classroom)
            # image_list = request.FILES.getlist('image_path')
            # for image in image_list:
            #     item = HomeworkFile.objects.create(homework=homework, image=image)
            #     item.save()
            # 사진파일까지 저장되도록 한 번 더 저장
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 숙제 상세 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def homework_detail(request, homework_id):
    homework = get_object_or_404(Homework, pk=homework_id)

    if request.method == 'GET':
        serializer = HomeworkSerializer(homework)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HomeworkSerializer(homework, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        homework.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    

# 제출한 숙제 상세 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def submit(request):
    if request.method == 'GET':
        submits = get_list_or_404(SubmitHomework, user=request.user)
        serializer = SubmitHomeworkSerializer(submits, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubmitHomeworkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)