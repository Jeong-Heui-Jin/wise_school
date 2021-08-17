from django.urls import path
from . import views

app_name = 'homework'

urlpatterns = [
    path('list/', views.homework_list, name='homework_list'),
    path('file/<int:homework_id>/', views.homeworkfile, name='homeworkfile'),
    path('detail/<int:homework_id>/', views.homework_detail, name='homework_list'),
    path('submit-detail/<int:submithomework_id>/', views.submit_detail, name='submit_detail'),
    path('submit/', views.submit, name='submit'),
    path('submit/file/<int:submithomework_id>/', views.submithomeworkfile, name='submithomeworkfile'),
]