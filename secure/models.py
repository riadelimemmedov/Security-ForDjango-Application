from django.db import models

# Create your models here.

#!Book
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.book_name)
