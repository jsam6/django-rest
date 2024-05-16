from django.db import models
from game.models import Game

class Player(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60, null=True, default=None)
    email =  models.CharField(max_length=120)
    password = models.TextField()

    # games = db.relationship('Game', secondary="user_game", back_populates='users') # many to many
    POSITIONS = {
        "S": "Small",
        "M": "Medium",
        "D": "Large",
        "GK": "Goalkeeper",
    }
    position = models.CharField(max_length=3, choices=POSITIONS)
    games = models.ManyToManyField(Game, related_name='players')

    def __str__(self):
        return self.id
    
    class Meta:
        db_table="player"