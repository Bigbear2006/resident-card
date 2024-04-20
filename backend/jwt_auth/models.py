from django.contrib.auth.models import AbstractUser
from django.db import models

from .fields import EncryptedField


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name', 'middle_name',
        'phone', 'birthday', 'passport_series', 'passport_number'
    ]
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    birthday = models.DateField()
    passport_series = EncryptedField()
    passport_number = EncryptedField()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
