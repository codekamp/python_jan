from django.db import models

class Activity(models.Model):
    time = models.TimeField()