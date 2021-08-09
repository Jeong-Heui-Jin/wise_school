from accounts.views import Parents
from .models import Timetable, TimetableDetail
from rest_framework import serializers



class TimetableDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimetableDetail
        fields = ('id', 'period', 'mon', 'tue', 'wed', 'thu', 'fri',)
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