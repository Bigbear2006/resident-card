from django.db import models

from jwt_auth.models import User
from . import utils


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    age_limit = models.CharField(max_length=5)
    address = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, 'events', through='CategoryEvent')
    ticket_count = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class CategoryEvent(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    event = models.ForeignKey(Event, models.CASCADE)


class Ticket(models.Model):
    event = models.ForeignKey(Event, models.CASCADE, 'tickets')
    owner = models.ForeignKey(User, models.CASCADE, 'tickets')


class Card(models.Model):
    number = models.BigIntegerField(default=utils.make_card_number)
    cvv = models.IntegerField(default=utils.make_cvv)
    owner = models.ForeignKey(User, models.CASCADE, 'cards')
    for_kid = models.BooleanField(default=False)
    status = models.CharField(max_length=100, default='Отправлена на модерацию')
    category = models.CharField(max_length=100)
    certificate = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return str(self.number)


class Hospital(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title


class Bank(models.Model):
    title = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title
