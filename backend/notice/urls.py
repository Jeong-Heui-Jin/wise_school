from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.notice, name='notice'),
    path('<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('notification/<int:user_id>/', views.notification, name='notification'),
    path('notification/<int:notification_id>/', views.notification_detail, name='notification_detail'),
]