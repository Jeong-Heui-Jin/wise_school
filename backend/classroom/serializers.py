from accounts.views import Parents
from .models import Timetable, TimetableDetail
from django.db.models import fields
from rest_framework import serializers
# from django.contrib.auth import get_user_model

# User = get_user_model()


class TimetableDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimetableDetail
        fields = ('id', 'period', 'mon', 'tue', 'wed', 'thu', 'fri',)
        read_only_fields = ('timetable',)


# class TimetableDetailListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = TimetableDetail
#         fields = ('id', 'period', 'mon', 'tue', 'wed', 'thu', 'fri',)
#         read_only_fields = ('timetable',)


class TimetableSerializer(serializers.ModelSerializer):
    timetabledetail_set = TimetableDetailSerializer(many=True)

    class Meta:
        model = Timetable
        fields = ('id', 'title',)
        read_only_fields = ('classroom',)


# class TimetableListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Timetable
#         fields = ('id', 'title',)
#         read_only_fields = ('classroom',)