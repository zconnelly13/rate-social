from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 256)
    profile_picture = models.URLField()
    rating = models.FloatField()
    friends = models.ManyToManyField('User')
    def __str__(self):
        return self.name

class Rating(models.Model):
    rater = models.ForeignKey('User',related_name='user_rater')
    ratee = models.ForeignKey('User',related_name='user_ratee')
    comment = models.CharField(max_length = 128)
    number = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{rater} rated {ratee}: {number} - '{comment}'".format(rater=self.rater,ratee=self.ratee,number=self.number,comment=self.comment)
