from django.db import models
from game.models import Game


class Field(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    address = models.TextField()
    postal_code = models.CharField(max_length=200)
    max_number = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='fields')

    
    def __str__(self):
        return self.id

    class Meta:
        db_table="field"
