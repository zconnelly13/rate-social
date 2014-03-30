from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 256)
    profile_picture = models.URLField()
    rating = models.FloatField()
    friends = models.ManyToManyField('User')

class Rating(models.Model):
    rater = models.ForeignKey('User',related_name='user_rater')
    ratee = models.ForeignKey('User',related_name='user_ratee')
    comment = models.CharField(max_length = 128)
    number = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
