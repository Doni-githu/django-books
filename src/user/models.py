from django.db import models
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    createdAt = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name
    