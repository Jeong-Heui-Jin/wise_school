import homework
from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
# from imagekit.models.fields import ProcessedImageField


class Homework(models.Model):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    # image = ProcessedImageField(format='JPEG', options={'quality': 90})


def homework_file_path(instance, filename):
    return '{0}/homework/{1}/{2}'.format(instance.homework.classroom.school.name, instance.homework.id, filename)

class HomeworkFile(models.Model):
    homework = models.ForeignKey(Homework, on_delete=CASCADE)
    image = models.ImageField(blank=True, upload_to=homework_file_path)


class SubmitHomework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)


def submit_file_path(instance, filename):
    return '{0}/homework/{1}/{2}/{3}'.format(instance.submithomework.homework.classroom.school.name, instance.submithomework.homework.id, instance.submithomework.student.username, filename)


class SubmitHomeworkFile(models.Model):
    submithomework = models.ForeignKey(SubmitHomework, on_delete=CASCADE)
    image = models.ImageField(blank=True, upload_to=submit_file_path)