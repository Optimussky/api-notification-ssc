from django.db import models
from django.contrib.auth.models import User
import uuid


class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class SendEmail(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    body = models.TextField()
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title