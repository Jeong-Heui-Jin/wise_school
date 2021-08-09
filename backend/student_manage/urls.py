from django.urls import path
from . import views

app_name = 'student_manage'

urlpatterns = [
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/detail/<int:attendance_id>/', views.attendance_detail, name='attendance_detail'),
    path('change/<int:attendancechange_id>/', views.attendance_change, name='attendance_change'),
    path('note/<int:student_id>/', views.note, name='note'),
    path('note/detail/<int:note_id>/', views.note_detail, name='note_detail'),
]