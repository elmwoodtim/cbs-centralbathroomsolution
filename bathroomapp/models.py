from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    points = models.IntegerField(default=0)

    def __repr__(self):
        return self.user.username + " " + str(self.points)

    def __str__(self):
        return self.user.username + " " + str(self.points)


class Bathroom(models.Model):
    bathroomId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    gender = models.CharField(max_length=6)
    numStall = models.IntegerField()
    numUrinal = models.IntegerField()
    reqCode = models.CharField(max_length=3)
    securityCode = models.CharField(max_length=10)
    ratingOverall = models.IntegerField()

    def __str__(self):
        return str(self.bathroomId) + " " + self.description + " " + self.gender + " " + str(self.ratingOverall)


class Packages(models.Model):
    packageId = models.CharField(max_length=3)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    min_bid = models.IntegerField()

    def __str__(self):
        return self.packageId + " " + self.location


class Bids(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.PROTECT)
    package = models.CharField(max_length=3)
    bid = models.IntegerField()

    def __str__(self):
        return self.user.user.username + " " + self.package + " " + str(self.bid)
