from .models import Timetable, TimetableDetail, Classroom
from rest_framework import serializers



class TimetableDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimetableDetail
        fields = ('id', 'time', 'mon', 'tue', 'wed', 'thu', 'fri', 'start', 'end',)
        read_only_fields = ('timetable',)


class TimetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timetable
        fields = ('id', 'title',)
        read_only_fields = ('classroom',)


class TimetableListSerializer(serializers.ModelSerializer):
    details = TimetableDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Timetable
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = '__all__'