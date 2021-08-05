from django.db import models
from django.contrib.auth.models import AbstractUser



def profile_image_path(instance, filename):
    return '{0}/profile/{1}'.format(instance.user.classroom.school.name, filename)



class User(AbstractUser):
    # id = models.IntegerField(primary_key=True)
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=20, null=True)     # 이름 (아이디는 username)
    usertype = models.IntegerField(null=True)
    phone = models.CharField(max_length=50, null=True)
    is_message = models.BooleanField(default=False, null=True)
    is_notification = models.BooleanField(default=False, null=True)
    image = models.ImageField(null=True, upload_to=profile_image_path)

    def __str__(self):
        return self.name


class StudentInfo(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='info')
    number = models.IntegerField()
    address = models.CharField(max_length=100)
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