from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()