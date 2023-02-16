from django.db import models

class GamePhoto(models.Model):

    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player_photo')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game_photo')
    photo_url = models.URLField(max_length=200)