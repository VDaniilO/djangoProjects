from django.db import models

# Create your models here.

class Number_info(models.Model):

    number = models.IntegerField()
    color = models.CharField(max_length=150, blank = True, null = True)

    def __str__(self):
        return self.color
