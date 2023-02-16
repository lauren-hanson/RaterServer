from django.db import models

class GameReview(models.Model):

    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player_review')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game_review')
    review = models.CharField(max_length=300)
    date_reviewed = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)