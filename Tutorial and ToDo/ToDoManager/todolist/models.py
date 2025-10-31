from django.db import models

# Create your models here.

#creating a model like table structure
class task(models.Model):
    task = models.CharField(max_length=200)
    is_completed = models.BooleanField()
