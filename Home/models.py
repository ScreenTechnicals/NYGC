from django.db import models
from datetime import datetime    

# Create your models here.

class Greeting_Card(models.Model):
    user_id = models.TextField(default=0)
    sender = models.CharField(max_length=100)
    reciver = models.CharField(max_length=100)
    greeting_message = models.TextField()
    datetime = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.sender
    