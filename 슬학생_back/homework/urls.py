from django.urls import path
from . import views

app_name = 'homework'

urlpatterns = [
    path('index/<int:class_id>/', views.homework_list, name='homework_list'),
    path('detail/<int:homework_id>/', views.homework_detail, name='homework_list'),
    path('submit/<int:submithomework_id>/', views.submit_detail, name='submit_detail'),
    path('submit-students/<int:homework_id>/', views.students_list, name='students_list'),   # (선생님) 숙제 기준, 제출한 학생 보기
    path('submit-list/<str:username>/', views.submit_list, name='submit_list'),   # (학생) 학생 기준, 제출한 숙제 보기
    # username / user_id 중 뭐로 할지 통일하기
]