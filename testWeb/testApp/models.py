from django.db import models

# Create your models here.
class testApp(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    poll = models.ForeignKey(testApp)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Pastie(models.Model):
    text = models.CharField(max_length=1024)
    time_stamp = models.DateTimeField('date published')
