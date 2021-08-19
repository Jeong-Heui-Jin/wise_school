from os import name
from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # 신규 신청
    path('servicere-quest/', views.service_request, name='service_request'),   # 서비스 신청

    # 학생/선생님
    path('login/', obtain_jwt_token),   # 로그인
    path('user-confirm/', views.user_confirm, name='user_confirm'),         # 사용자 정보 확인 (비밀번호 재설정 전 단계)
    path('password-reset/', views.password_reset, name='password_reset'),   # 비밀번호 재설정
    path('change-password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),

    path('class-members/', views.class_members, name='class_members'),
    path('info/<int:user_id>/', views.info, name='info'),   # 선생님/학생 정보
    path('parents/<int:user_id>/', views.parents_list, name='parents_list'),   # 비상연락망 목록
    path('parents/detail/<int:parent_id>/', views.parent_detail, name='parent_detail'),   # 비상연락망 상세보기
    path('teachers/', views.teachers, name='teachers'),   # 전체 선생님 목록
    path('students/', views.students, name='students'),   # 전체 학생 목록
    path('signup/', views.signup, name='signup'),
    path('image-change/<int:user_id>/', views.image_change, name='image_change'),

    # path('create-students/<int:school_id>/', views.create_students),   # 학생 계정 생성 (서비스측)
    # path('create-teachers/<int:school_id>/', views.create_teachers),   # 선생님 계정 생성 (서비스측)
    # path('<str:username>/', views.student, name='student'),   # 학생 정보 관리 (관리자)
]