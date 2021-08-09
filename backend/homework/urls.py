from django.urls import path
from . import views

app_name = 'homework'

urlpatterns = [
    path('list/', views.homework_list, name='homework_list'),
    path('detail/<int:homework_id>/', views.homework_detail, name='homework_list'),
    path('submit-detail/<int:submithomework_id>/', views.submit_detail, name='submit_detail'),
    path('submit/', views.submit_list, name='submit_list'),   # (학생) 학생 기준, 제출한 숙제 보기
]