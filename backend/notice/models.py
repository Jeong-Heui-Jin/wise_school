from django.db import models
from django.conf import settings


class Notice(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)
    is_important = models.BooleanField(default=False)
    
    
def notice_file_path(instance, filename):
    return '{0}/notice/{1}/{2}'.format(instance.notice.classroom.school.name, instance.notice.id, filename)


class NoticeFile(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    path = models.ImageField(blank=True, upload_to=notice_file_path)


class Notification(models.Model):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)