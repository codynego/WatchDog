from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from data_manager.models import Server

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
    

