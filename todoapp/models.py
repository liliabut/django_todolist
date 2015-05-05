from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='Normal')
    fortschritt = models.IntegerField(default=0)
    start = models.DateTimeField('start')
    frist = models.DateTimeField('frist')
    