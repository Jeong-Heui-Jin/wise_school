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
        # fields = ('id', 'title', 'content', 'registertime', 'is_important',)
        fields = '__all__'
        read_only_fields = ('classroom', 'teacher',)

class NoticeFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticeFile
        fields = ('image', 'notice',)
        # read_only_fields = ('homework',)

class NoticeListSerializer(serializers.ModelSerializer):
    noticefile_set = NoticeFileSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id', 'classroom', 'content', 'registertime',)
        read_only_fields = ('student',)