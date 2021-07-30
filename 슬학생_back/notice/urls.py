from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('<int:class_id>/', views.notice_list),
    path('<int:notice_id>/', views.notice_detail),
    path('<str:username>/notification/', views.notification_list),
    path('<str:username>/notification/<int:notification_id>/', views.notification_detail),
]