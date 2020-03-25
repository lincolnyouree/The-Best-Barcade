from django.db import models
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

CONDITIONS = (
    ('1', 'Unplayable'),
    ('2', 'Poor'),
    ('3', 'Acceptable'),
    ('4', 'Good'),
    ('5', 'Excellent')
)

PRICE = (
    ('1', '$'),
    ('2', '$$'),
    ('3', '$$$')
)

class Bar(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price_range = models.CharField(
        max_length=1,
        choices=PRICE,
        default=PRICE[0][0]
    )
    has_food = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bar_details', kwargs={'bar_id': self.id})

class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    number_of_players = models.CharField(max_length=10)
    condition = models.CharField(
    max_length=1,
    choices=CONDITIONS,
    default=CONDITIONS[0][0]
    )
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    comments = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_details', kwargs={'game_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"