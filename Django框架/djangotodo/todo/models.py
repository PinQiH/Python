from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)  #標題
    finish = models.BooleanField(default=False)  #是否完成
    created = models.DateField(default=timezone.now)  #建立日期