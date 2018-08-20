from django.db import models


# Create your models here.
class Speed(models.Model):
    speed = models.IntegerField(default=0)
