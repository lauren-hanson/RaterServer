from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    designer = models.CharField(max_length=200)
    year_released = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    num_of_players = models.IntegerField()
    estimated_time = models.IntegerField()
    recommended_age = models.IntegerField()
