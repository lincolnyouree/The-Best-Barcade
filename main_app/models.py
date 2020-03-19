from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CONDITIONS = (
#     ('1', 'Unplayable')
#     ('2', 'Poor'),
#     ('3', 'Acceptable'),
#     ('4', 'Good'),
#     ('5', 'Excellent')
# )

class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    number_of_players = models.CharField(max_length=10)
    condition = models.CharField(max_length=20)
    # max_length=1,
    # choices=CONDITIONS,
    # default=CONDITIONS[2][2]
    # )
    comments = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bar(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price_range = models.CharField(max_length=10)
    has_food = models.BooleanField
    games = models.ForeignKey(Game, on_delete=models.CASCADE)