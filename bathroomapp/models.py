from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    points = models.IntegerField(default=0)

    def __repr__(self):
        return self.user.username + " " + str(self.points)

    def __str__(self):
        return self.user.username + " " + str(self.points)

