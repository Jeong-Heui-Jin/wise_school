from django.db.models import manager
from django.http.response import JsonResponse
from .models import User, Parents
from classroom.models import School, Classroom
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParentSerializer, UserSerializer, UserListSerializer, ServiceRequestSerializer, SignupSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# 신규 서비스 신청
@api_view(['POST',])
def service_request(request):
    serializer = ServiceRequestSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 해당 정보가 전부 한 사용자를 가리키면, 그 사용자 객체를 넘겨줌.
@api_view(['POST',])
def user_confirm(request):
    username = request.data.get('username')
    user = get_object_or_404(User, username=username)
    if user.name == request.data.get('name') and user.phone == request.data.get('phone'):
        serializer = UserSerializer(user)
        return Response(serializer.data)
    # 일치하지 않을 경우 에러 발생
    return Response({'error': '사용자 정보가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 비밀번호 재설정
@api_view(['POST',])
def password_reset(request):
    username = request.data.get('username')
    new_password = request.data.get('password')
    # 일치 여부는 front에서 확인해서 넘겨주면 될 듯.
    # password_confirm = request.data.get('passwordConfirmation')

    user = get_object_or_404(get_user_model(), username=username)
    user.set_password(new_password)
    user.save()
    return Response({'user':user,})


@api_view(['POST', 'GET',])
def change_password(request):
    form = PasswordChangeForm(request.user, request.data)
    # old_password, new_password1, new_password2
    if form.is_valid():
        form.save()
        # 비밀번호 변경 후에도 로그인 유지할 수 있도록
        update_session_auth_hash(request, form.user)
        return Response({'success' : '비밀번호 변경 성공'})
    return Response({'error': '비밀번호가 올바르지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 해당 사용자의 정보 조회/수정/삭제
@api_view(['GET', 'PUT','DELETE',])
def info(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserListSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 해당 학생의 보호자들 목록 조회 / 추가
@api_view(['GET', 'POST'])
def parents_list(request, user_id):
    parents_list = get_list_or_404(Parents, pk=user_id)
    serializer = ParentSerializer(parents_list, many=True)
    return Response(serializer.data)


# 보호자 상세 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE',])
def parent_detail(request, parent_id):
    parent = get_object_or_404(Parents, pk=parent_id)
    if request.method == 'GET':
        serializer = ParentSerializer(parent)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        parent.delete()
        data = {
            'delete': '삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 반 친구들 + 선생님 목록 조회
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def class_members(request):
    classroom = request.user.classroom
    class_members = get_list_or_404(User, classroom=classroom)
    serializer = UserSerializer(class_members, many=True)
    return Response(serializer.data)


# 해당 학교의 선생님들 목록 조회 (학교 관리자)
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def teachers(request):
    # 해당 사용자가 속한 학교
    school = request.user.classroom.school
    # 그 학교에 속한 선생님들(usertype=1인 user들) 목록
    teachers_list = get_user_model().objects.filter(classroom__school=school, usertype=1)
    serializer = UserSerializer(teachers_list, many=True)
    return Response(serializer.data)


# 해당 학교의 학생들 목록 조회 (학교 관리자)
@api_view(['GET',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def students(request):
    # 해당 사용자가 속한 학교
    school = request.user.classroom.school
    # 그 학교에 속한 학생들(usertype=2인 user들) 목록
    students_list = get_user_model().objects.filter(classroom__school=school, usertype=2)
    serializer = UserSerializer(students_list, many=True)
    return Response(serializer.data)


# 학생 계정 생성
@api_view(['POST'])
def create_student(request, school_id):
    school = get_object_or_404(School, pk=school_id)

    students_num = int(request.data.get('students_num'))
    i = 0
    for _ in range(students_num):
        user = User(id=i, usertype=2, classroom_school_id=school)
        user.save()
        i += 1

    teachers_num = int(request.data.get('teachers_num'))
    for _ in range(teachers_num):
        user = User(id=i, usertype=1, classroom_school=school)
        user.save()
        i += 1

    return Response({'created':'계정이 생성되었습니다.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    class_id = request.data.get('class_id')
    room = get_object_or_404(Classroom, pk=class_id)

    serializer = SignupSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        
        user.set_password(password)
        user.classroom = room
        user.save()
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)