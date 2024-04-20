from django.db import models

from jwt_auth.models import User


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
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Ticket(models.Model):
    price = models.IntegerField()
    event = models.ForeignKey(Event, models.CASCADE, 'tickets')
    owner = models.ForeignKey(User, models.CASCADE, 'tickets')


class Card(models.Model):
    number = models.BigIntegerField()
    cvv = models.IntegerField()
    owner = models.ForeignKey(User, models.CASCADE, 'cards')
    for_kid = models.BooleanField()
    status = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    certificate = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.number


class Bid(models.Model):
    card = models.OneToOneField(Card, models.CASCADE, related_name='bid')
    staff = models.ForeignKey(User, models.SET_NULL, 'bids', null=True)
