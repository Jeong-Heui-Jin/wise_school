from django.db import models
from django.contrib.auth.models import AbstractUser
# from imagekit.models import ProcessedImageField, ImageSpecField
# from imagekit.processors import ResizeToFit



class User(AbstractUser):
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.PROTECT, related_name='classmembers')
    name = models.CharField(max_length=20)
    usertype = models.IntegerField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    is_Message = models.BooleanField()
    image = models.ImageField(blank=True, upload_to='postings/%Y%M%d')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studentinfos')
    number = models.IntegerField()
    address = models.CharField(max_length=100)
    is_notification = models.BooleanField()


class Parents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return self.relation