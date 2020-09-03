from django.db import models


# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=10)
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ISBN
