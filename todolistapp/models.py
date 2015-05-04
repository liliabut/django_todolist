from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc =  models.CharField(max_length=200)
    prio =  models.CharField(max_length=20)    
    progress = models.IntegerField(default=0)
    status =  models.CharField(max_length=200,default="Neu")
    start_date = models.DateTimeField('date published')
    due_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title