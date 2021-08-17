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

    class Meta:
        model = SubmitHomework
        fields = ('id', 'content', 'registertime',)
        read_only_fields = ('homework', 'student',)


class SubmitHomeworkListSerializer(serializers.ModelSerializer):
    submithomeworkfile_set = SubmitHomeworkFileSerializer(many=True, read_only=True)

    class Meta:
        model = SubmitHomework
        fields = '__all__'


class HomeworkFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeworkFile
        fields = ('image', 'homework',)
        # read_only_fields = ('homework',)


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = '__all__'
        read_only_fields = ('classroom',)


class HomeworkListSerializer(serializers.ModelSerializer):
    homeworkfile_set = HomeworkFileSerializer(many=True, read_only=True)
    submithomework_set = SubmitHomeworkListSerializer(many=True, read_only=True)
    submithomework_count = serializers.IntegerField(source='submithomework_set.count', read_only=True)

    class Meta:
        model = Homework
        fields = '__all__'