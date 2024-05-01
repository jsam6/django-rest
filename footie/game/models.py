from django.db import models

class Game(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description =  models.TextField()
    date = models.DateField()
    time = models.TimeField()
    repeat = models.BooleanField(default=False)
    cost = models.FloatField(default=0)
    
    max_player = models.IntegerField(default=12)
    min_player = models.IntegerField(default = 0)
    # created_by
    private = models.BooleanField(default=False)
    keyword = models.TextField(default="[]")
    # users
    # field_id

    
    def __str__(self):
        return self.id

    class Meta:
        db_table="game"

    
    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(80), nullable=False)
    # description = db.Column(db.String(120), nullable=True)
    # date = db.Column(db.String(50), nullable=True)
    # time = db.Column(db.String(10), nullable=True)
    # datetime = db.Column(db.DateTime(timezone=True), nullable=False)
    # repeat = db.Column(db.Boolean, nullable=True)
    # cost = db.Column(db.Float, nullable=True)
    # max_player = db.Column(db.Integer, default=0)
    # created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # private = db.Column(db.Boolean, default=False)
    # keyword = db.Column(db.String, default="[]")
    # users = db.relationship('User', secondary="user_game", back_populates='games') # many to many
    # field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False) # One-to-Many
    # price = db.Column(db.Integer, default=0)