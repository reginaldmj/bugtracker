from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import timezone
from datetime import datetime
from django.utils import timezone

# Create your models here.

class MyUser(AbstractUser):
    homepage = models.URLField(null=True, blank=True)
    display_name = models.CharField(max_length=40, null=True, blank=True)
    age = models.IntegerField(default=115)

    def __str__(self):
        return self.username

class MyTicket(models.Model):
    NEW = 'N'
    IN_PROGRESS = 'P'
    DONE = 'D'
    INVALID = 'I'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In_Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]

    title = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES,
    )
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)
    user_assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE, null=True, )
    user_who_completed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.title