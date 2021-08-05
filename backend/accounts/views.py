from django.db.models import manager
from django.http.response import JsonResponse
from .models import User, Parents
from classroom.models import School
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParentSerializer, UserSerializer, UserListSerializer, ServiceRequestSerializer, SignupSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



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
    user = get_object_or_404(get_user_model(), username=username)
    if user.name == request.data.get('name') and user.phone == request.data.get('phone'):
        user_info = {
            'user' : user,
        }
        return JsonResponse(user_info)
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
    user = get_object_or_404(get_user_model(), pk=user_id)
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


# 해당 학교의 선생님들 목록 조회 (학교 관리자)
def teachers(request, school_id):
    teachers_list = get_user_model().objects.filter(classroom_school_id=school_id, usertype=1)
    serializer = UserListSerializer(teachers_list, many=True)
    return Response(serializer.data)


# 해당 학교의 학생들 목록 조회 (학교 관리자)
def students(request, school_id):
    students_list = get_user_model().objects.filter(classroom_school_id=school_id, usertype=2)
    serializer = UserListSerializer(students_list, many=True)
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
	#1-1. Client에서 온 데이터를 받아서
    # id = request.data.get('id')
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = SignupSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)