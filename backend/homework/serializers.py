from .models import Homework, HomeworkFile, SubmitHomework, SubmitHomeworkFile
from django.db.models import fields
from rest_framework import serializers

# from django.contrib.auth import get_user_model
# User = get_user_model()



class SubmitHomeworkFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmitHomeworkFile
        fields = '__all__'


class SubmitHomeworkSerializer(serializers.ModelSerializer):
    file_set = SubmitHomeworkFileSerializer(many=True)

    class Meta:
        model = SubmitHomework
        fields = ('id', 'content', 'registertime', 'file_set',)
        read_only_fields = ('homework', 'student',)


class HomeworkFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeworkFile
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    # file_set = HomeworkFileSerializer(many=True, read_only=True)
    # submit_set = SubmitHomeworkSerializer(many=True, read_only=True)
    # submit_count = serializers.IntegerField(source='submit_set.count', read_only=True)

    class Meta:
        model = Homework
        fields = '__all__'
        read_only_fields = ('classroom',)