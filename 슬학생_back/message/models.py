from django.db import models
from django.conf import settings
from django.db.models.deletion import PROTECT


class Message(models.Model):
    # OneToOneField 고려
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    message = models.TextField()
    sendtime = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=True)