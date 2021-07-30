from django.urls import path
from . import views

app_name = 'student_manage'

urlpatterns = [
    path('<int:class_id>/<str:date>/attendance/', views.attendance_list),
    path('<int:student_id>/<str:date>/attendance/', views.attendance_detail),
    path('<int:student_id>/<str:date>/attendance-change/', views.attendance_change),
    path('<int:student_id>/note/', views.note_list),
    path('<int:student_id>/note/<int:note_id>/', views.note_detail),
]