# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from .models import Notice, Notification
# from homework.models import Homework
# from .serializers import NotificationSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status



# @receiver(post_save, sender=Notice)
# @receiver(post_save, sender=Homework)
# @api_view(['POST',])
# def add_notification(sender, **kwargs):
#     new = kwargs['instance']
#     notification = Notification()
#     notification.classroom = new.classroom

#     if sender == Notice:
#         notification.content = '공지사항(' + new.title + ')이 추가되었습니다.'
#     elif sender == Homework:
#         notification.content = '숙제(' + new.title + ')가 추가되었습니다.'

#     # 해당 반 학생들 명단 가져오기
#     students = new.classroom.student_set
#     for student in students:
#         # 각 학생마다 알림 보내기
#         notification.student = student
#         serializer = NotificationSerializer(data=notification)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # 알림 받은 학생의 is_notification값은 True로 바꿔주기
#             student.info.is_notification = True
#             student.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)