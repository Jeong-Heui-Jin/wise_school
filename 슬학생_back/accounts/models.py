from django.db import models
from django.contrib.auth.models import AbstractUser
# from imagekit.models import ProcessedImageField, ImageSpecField
# from imagekit.processors import ResizeToFit



class User(AbstractUser):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.PROTECT, related_name='classmembers')
    name = models.CharField(max_length=20)     # 아이디
    usertype = models.IntegerField()           # 타입(관리자/선생님/학생)
    phone = models.CharField(max_length=50)    # 연락처
    # email = models.EmailField()                # 이메일
    is_message = models.BooleanField()         # 메시지 체크 여부
    image = models.ImageField(blank=True, upload_to='profileimages/%Y%M%d')
    # image = ProcessedImageField(
    #     upload_to='postings/resize/%Y%m%d',
    #     processors=[ResizeToFit(width=960, upscale=False)],
    #     format='JPEG'
    # )
    # image_thumbnail = ImageSpecField(
    #     source='image',
    #     processors=[ResizeToFit(width=320, upscale=False)],
    #     format='JPEG',
    #     options={'quality': 60}
    # )

    def __str__(self):
        return self.name


class StudentInfo(models.Model):
    # OneToOneField 고려
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studentinfos')
    number = models.IntegerField()
    address = models.CharField(max_length=100)
    is_notification = models.BooleanField(default=False)


class Parents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return self.relation


class ServiceRequest(models.Model):
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    password_confirmation = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    school_name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name