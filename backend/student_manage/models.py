# from student_manage.views import attendance
from django.db import models
from django.conf import settings


class Note(models.Model):
    student = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='notes')
    teacher = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='wrote_notes')
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    student = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    registertime = models.DateTimeField(auto_now_add=True)


def attendance_change_file_path(instance, filename):
    return '{0}/notice/{1}/{2}'.format(instance.attendance.classroom.school.name, instance.attendance.classroom.school.name, filename)


class AttendanceChange(models.Model):
    attendance = models.OneToOneField(Attendance, on_delete=models.CASCADE)
    reason = models.TextField()
    image = models.ImageField(blank=True, upload_to=attendance_change_file_path)
    registertime = models.DateTimeField(auto_now_add=True)