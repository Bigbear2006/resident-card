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
    categories = models.ManyToManyField(Category, 'events')
    ticket_count = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Ticket(models.Model):
    event = models.ForeignKey(Event, models.CASCADE, 'tickets')
    owner = models.ForeignKey(User, models.CASCADE, 'tickets')


class Card(models.Model):
    number = models.BigIntegerField(default=utils.make_card_number)
    cvv = models.IntegerField(default=utils.make_cvv)
    owner = models.ForeignKey(User, models.CASCADE, 'cards')
    for_kid = models.BooleanField()
    status = models.CharField(max_length=100, default='Отправлена на модерацию')
    category = models.CharField(max_length=100)
    certificate = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.number


class Bid(models.Model):
    card = models.OneToOneField(Card, models.CASCADE, related_name='bid')
    staff = models.ForeignKey(User, models.SET_NULL, 'bids', null=True)


class Hospital(models.Model):
    title = models.CharField(max_length=255)
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
