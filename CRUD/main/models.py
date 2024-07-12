from django.db import models
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length = 25)
    actor = models.CharField(max_length = 25)
    story = models.CharField(max_length =255)
    redate = models.DateField(auto_now=True)
    