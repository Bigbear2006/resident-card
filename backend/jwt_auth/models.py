from django.contrib.auth.models import AbstractUser
from django.db import models

from .fields import EncryptedField


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username', 'phone', 'birthday', 'passport_series', 'passport_number'
    ]
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, null=True)
    birthday = models.DateField()
    passport_series = EncryptedField()
    passport_number = EncryptedField()

    def get_full_name(self):
        return self.username
