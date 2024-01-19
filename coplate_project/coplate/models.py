from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
from django.conf import settings


# Create your models here.

class User(AbstractUser):

    nickname = models.CharField( # 학번
        max_length=20, 
        unique=False, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique' : '이미 존재하는 학번입니다.'},
    )

    department = models.CharField( # 학과(학부)
        max_length=20, 
        unique=False, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique' : '이미 존재하는 학과(학부)입니다.'},
    )

    def __str__(self):
        return self.email
    
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Community(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Adboard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Taxi(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class ClubApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default='')
    club_name = models.CharField(max_length=100, null=True, default='')
    applied = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'club_name')

    def __str__(self):
        return str(self.user)
