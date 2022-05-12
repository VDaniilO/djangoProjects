from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):

    nameUsr = models.CharField(max_length=150)  # user name
    message = models.TextField(blank=True)  # message field
    verify =  models.BooleanField(default=False)  # status verify message
    condition = models.ForeignKey('Conditions', on_delete=models.PROTECT, null=True, default="1")  # status cond
    user_permission = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameUsr

class Conditions(models.Model):

    name = models.CharField(max_length=150)  # condition name

    def __str__(self):
        return self.name
