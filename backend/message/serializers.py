from .models import Message
from django.db.models import fields
from rest_framework import serializers



# class MessageListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Message
#         fields = ('id', 'sender', 'receiver', 'message', 'sendtime', 'is_checked',)


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message', 'sendtime', 'is_checked',)
        read_only_fields = ('sender', 'receiver',)