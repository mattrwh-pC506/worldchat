from django.db import models
from django.contrib.auth.models import User

class Chatter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    geocode = models.CharField(max_length=50)
    usertag = models.CharField(max_length=50)
    address = models.CharField(max_length=200, default="")
    online = models.BooleanField(default=False)
