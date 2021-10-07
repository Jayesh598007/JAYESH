from django.db import models
from django.db.models.fields import DateField, TextField


# makemigrations -- create and store the chnages in the file
# migrate -- save and apply the changes created by makemigrations


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

