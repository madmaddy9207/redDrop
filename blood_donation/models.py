# models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

class RequestBlood(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    blood_group = models.CharField(max_length=10)
    date = models.DateField(max_length=10)

    def __str__(self):
        return f"{self.name}'s Blood Request on {self.date}"
   
