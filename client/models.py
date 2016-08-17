from django.db import models

class Searcher(models.Model):
    location = models.CharField(max_length=30)
    food = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.location, self.food)

