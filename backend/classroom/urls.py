from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('timetable-create/', views.timetable_create, name='timetable_create'),
    path('timetable/<int:timetable_id>/', views.timetable, name='timetable'),
    path('timetable-detail/<int:timetabledetail_id>/', views.timetable_detail, name='timetable_detail'),
]