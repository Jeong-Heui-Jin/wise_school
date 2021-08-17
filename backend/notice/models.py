from django.db import models
from django.conf import settings

from datetime import datetime
import boto3
from SHS.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class Notice(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)
    is_important = models.BooleanField(default=False)
    
    
def notice_file_path(instance, filename):
    image_time = (str(datetime.now())).replace(" ","") # 이미지이름을 시간으로 설정하기 위해 datetime를 사용했다.
    extension = os.path.splitext(filename)[-1].lower()
    image_url = "http://dycho96.s3.ap-northeast-2.amazonaws.com/"+image_time+"."+extension  # 업로드된 이미지의 url이 설정값으로 저장됨
    image_url = image_url.replace(" ","/")
    return image_url


class NoticeFile(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to=notice_file_path)


class Notification(models.Model):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    registertime = models.DateTimeField(auto_now_add=True)