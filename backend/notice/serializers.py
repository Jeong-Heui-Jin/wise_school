from .models import Notice, NoticeFile, Notification
from django.db.models import fields
from rest_framework import serializers

# from django.contrib.auth import get_user_model
# User = get_user_model()



class NoticeFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticeFile
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('id', 'title', 'content', 'registertime', 'is_important',)
        read_only_fields = ('classroom', 'teacher',)


class NoticeListSerializer(serializers.ModelSerializer):
    noticefile_set = NoticeFileSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id', 'classroom', 'student', 'content', 'registertime',)
        # read_only_fields = ('attendance',)