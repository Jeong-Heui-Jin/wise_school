from django.db import models


class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    id = models.IntegerField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')
    grade = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.grade


class Timetable(models.Model):
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)


class TimetableDetail(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='details')
    time = models.IntegerField()
    start = models.TimeField()
    end = models.TimeField()
    mon = models.TextField(blank=True, null=True)
    tue = models.TextField(blank=True, null=True)
    wed = models.TextField(blank=True, null=True)
    thu = models.TextField(blank=True, null=True)
    fri = models.TextField(blank=True, null=True)
    # 요일마다 교시 수가 다를 수 있으니까 blank=True