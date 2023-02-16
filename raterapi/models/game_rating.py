from django.db import models

class GameRating(models.Model):

    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player_rating')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game_rating')
    rating = models.IntegerField()
    date_rated = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)