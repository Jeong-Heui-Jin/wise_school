from django.db import models
from django.db.models.fields import IntegerField


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
        return self.name


class Timetable(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='timetables')
    title = models.CharField(max_length=20)


class TimetableDetail(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='timetable_details')
    period = models.IntegerField()
    monday = models.TextField()
    tuesday = models.TextField()
    wednesday = models.TextField()
    thursday = models.TextField()
    friday = models.TextField()