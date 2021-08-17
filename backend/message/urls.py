from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('<int:buddy_id>/', views.talk, name='talk'),
]