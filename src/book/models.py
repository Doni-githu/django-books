from django.db import models
from datetime import date



class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published = models.DateField(default=date.today)
    isbn = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
