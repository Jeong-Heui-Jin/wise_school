from django.db import models
from django.contrib.auth.models import AbstractUser



def profile_image_path(instance, filename):
    image_time = (str(datetime.now())).replace(" ","") # 이미지이름을 시간으로 설정하기 위해 datetime를 사용했다.
    extension = os.path.splitext(filename)[-1].lower()
    image_url = "http://dycho96.s3.ap-northeast-2.amazonaws.com/"+image_time+"."+extension  # 업로드된 이미지의 url이 설정값으로 저장됨
    image_url = image_url.replace(" ","/")
    return image_urls



class User(AbstractUser):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=20, null=True)     # 이름 (아이디는 username)
    usertype = models.IntegerField()
    phone = models.CharField(max_length=50, null=True)
    is_message = models.BooleanField(default=False, blank=True, null=False)
    is_notification = models.BooleanField(default=False, blank=True, null=False)
    image = models.ImageField(blank=True, null=True, upload_to=profile_image_path)

    def __str__(self):
        return self.name


class StudentInfo(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='info')
    number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    is_notification = models.BooleanField(default=False)


class Parents(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parents')
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return self.relation


class ServiceRequest(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    password_confirmation = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    school_name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name