from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('<int:class_id>/members/', views.members),
    path('<int:class_id>/timetable/', views.timetable),
    path('<int:class_id>/timetable/<int:timetabledetail_id>/', views.timetable),
]