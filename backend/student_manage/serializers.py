from .models import Note, Attendance, AttendanceChange
from django.db.models import fields
from rest_framework import serializers

# from django.contrib.auth import get_user_model
# User = get_user_model()



class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'content', 'registertime',)
        read_only_fields = ('student', 'teacher',)


class NoteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class AttendanceChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceChange
        fields = ('id', 'reason', 'image', 'registertime',)
        read_only_fields = ('attendance',)


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ('id', 'status', 'registertime',)
        read_only_fields = ('student', 'classroom',)


class AttendanceListSerializer(serializers.ModelSerializer):
    attendancechange = AttendanceChangeSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'