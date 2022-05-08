from django.db import models
from django.urls import reverse

# Create your models here.

class logInf(models.Model):

    login = models.CharField(max_length = 150)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 150)
    firstName = models.CharField(max_length = 150)
    lastName = models.CharField(max_length = 150)
    photo = models.ImageField(upload_to = 'photo/%Y/%m/%d/', blank = True)
    region = models.ForeignKey('Regions', on_delete = models.PROTECT, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    update_up = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse('profile', kwargs = {"usrInfo": self.login})

    def __str__(self):
        return self.login

class Regions(models.Model):

    Region_name = models.CharField(max_length = 150, db_index = True)

    def get_absolute_url(self):
        return reverse('regionUsr', kwargs = {"region_id": self.pk})

    def __str__(self):
        return self.Region_name
