from django.urls import path
from . import views

app_name = 'student_manage'

urlpatterns = [
    path('attendance/<int:class_id>/<str:date>/', views.attendance_list),
    path('attendance/detail/<int:student_id>/<str:date>/', views.attendance_detail),
    path('attendance-change/<int:student_id>/<str:date>/', views.attendance_change),
    path('note/<int:student_id>/', views.note_list),
    path('note/<int:student_id>/<int:note_id>/', views.note_detail),
]