from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('<int:class_id>/', views.notice_list, name='notice_list'),
    path('<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('notification/<int:user_id>/', views.notification_list, name='notification_list'),
    path('notification/<int:notification_id>/', views.notification_detail, name='notification_detail'),
]