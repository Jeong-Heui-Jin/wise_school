import homework
from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
# from imagekit.models.fields import ProcessedImageField

from datetime import datetime
import boto3
from SHS.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class Homework(models.Model):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    # image = ProcessedImageField(format='JPEG', options={'quality': 90})


def homework_file_path(instance, image):
    image_time = (str(datetime.now())).replace(" ","") # 이미지이름을 시간으로 설정하기 위해 datetime를 사용했다.
    extension = os.path.splitext(filename)[-1].lower()
    image_url = "http://dycho96.s3.ap-northeast-2.amazonaws.com/"+image_time+"."+extension  # 업로드된 이미지의 url이 설정값으로 저장됨
    image_url = image_url.replace(" ","/")
    return image_url

class HomeworkFile(models.Model):
    homework = models.ForeignKey(Homework, on_delete=CASCADE)
    image = models.ImageField(blank=True, upload_to=homework_file_path)


class SubmitHomework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)


def submit_file_path(instance, filename):
    image_time = (str(datetime.now())).replace(" ","") # 이미지이름을 시간으로 설정하기 위해 datetime를 사용했다.
    extension = os.path.splitext(filename)[-1].lower()
    image_url = "http://dycho96.s3.ap-northeast-2.amazonaws.com/"+image_time+"."+extension  # 업로드된 이미지의 url이 설정값으로 저장됨
    image_url = image_url.replace(" ","/")
    return image_url



class SubmitHomeworkFile(models.Model):
    submithomework = models.ForeignKey(SubmitHomework, on_delete=CASCADE)
    image = models.ImageField(blank=True, upload_to=submit_file_path)