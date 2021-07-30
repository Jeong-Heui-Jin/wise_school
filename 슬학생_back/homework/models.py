import homework
from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
# from imagekit.models.fields import ProcessedImageField


class Homework(models.Model):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    # image = ProcessedImageField(format='JPEG', options={'quality': 90})


class HomeworkFile(models.Model):
    homework = models.ForeignKey(Homework, on_delete=CASCADE)
    path = models.ImageField(blank=True, upload_to='homework/%Y%M%d')
    registertime = models.DateTimeField(auto_now_add=True)
    original_filename = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)


class SubmitHomework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)


class SubmitHomeworkFile(models.Model):
    submithomework = models.ForeignKey(SubmitHomework, on_delete=CASCADE)
    path = models.ImageField(blank=True, upload_to='submithomework/%Y%M%d')
    registertime = models.DateTimeField(auto_now_add=True)
    original_filename = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)