from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('classroom/', include('classroom.urls')),
    path('accounts/', include('accounts.urls')),
    path('student-manage/', include('student_manage.urls')),
    path('notice/', include('notice.urls')),
    path('homework/', include('homework.urls')),
    path('message/', include('message.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)