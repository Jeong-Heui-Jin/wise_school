from student_manage.views import attendance
from django.db import models
from django.conf import settings


class Note(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    note = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)


class AttendanceChange(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    reason = models.TextField()
    path = models.ImageField(blank=True, upload_to='attendance/%Y%M%d')
    registertime = models.DateTimeField(auto_now_add=True)
    original_filename = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)