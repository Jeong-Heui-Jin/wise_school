from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # 신규 신청
    path('servicere-quest/', views.service_request, name='service_request'),   # 서비스 신청

    # 학생/선생님
    path('login/', obtain_jwt_token),   # 로그인
    path('password-reset/', views.password_reset, name='password_reset'),   # 비밀번호 재설정 
    path('<str:user_id>/info/', views.info, name='info'),   # 선생님/학생 정보
    path('<str:user_id>/parents/', views.parents, name='parents'),   # 비상연락망
    path('<int:school_id>/teachers/', views.teachers, name='teachers'),   # 선생님 계정 생성
    path('<int:school_id>/students/', views.students, name='students'),   # 전체 학생 목록

    # NEW: custom verify-token view which is not included in django-rest-passwordreset
    # path('reset-password/verify-token/', views.CustomPasswordTokenVerificationView.as_view(), name='password_reset_verify_token'),
    # NEW: The django-rest-passwordreset urls to request a token and confirm pw-reset
    # path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # path('create-students/', views.create_students),   # 학생 계정 생성 (서비스측)
    # path('<str:username>/', views.student, name='student'),   # 학생 정보 관리 (관리자)
]