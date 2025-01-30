from django.db import models

# Create your models here.

class Level(models.Model):
    title = models.CharField(max_length=50)


class Agent(models.Model):
    name = models.CharField(max_length=120)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
