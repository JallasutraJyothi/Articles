from django.db import models

# Create your models here.
class Cards(models.Model):
    heading=models.CharField(max_length=100)
    description=models.CharField(max_length=800)