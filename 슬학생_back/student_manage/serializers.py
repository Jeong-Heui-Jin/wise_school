from .models import Note, Attendance, AttendanceChange
from django.db.models import fields
from rest_framework import serializers

# from django.contrib.auth import get_user_model
# User = get_user_model()



class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class AttendanceChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceChange
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    change_set = AttendanceChangeSerializer(many=True, read_only=True)

    class Meta:
        model = Attendance
        fields = ('id', 'reason', 'path', 'registertime', 'original_filename', 'filename', 'change_set',)
        read_only_fields = ('attendance',)