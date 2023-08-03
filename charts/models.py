from django.db import models

# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Richest(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
    net_worth = models.IntegerField()
    country = models.CharField(max_length=100)
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.name

