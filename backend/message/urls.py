from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('<int:receiver_id>/', views.message_list, name='message_list'),
    path('<int:sender_id>/<int:receiver_id>/', views.talk, name='talk'),
]