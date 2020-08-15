from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    phone_number = models.CharField(max_length=255, null=False)
    email_address = models.EmailField(default=None, null=False)
    is_admin = models.BooleanField(default=False)


class House(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=1000, null=False)
    price = models.FloatField(null=False)
    house_type = models.CharField(max_length=1000, null=False)
    meters = models.FloatField(null=False)
    bedrooms = models.IntegerField(null=False)
    parkings = models.IntegerField(null=False)
    location = models.CharField(max_length=1000, null=False)
    locality = models.CharField(max_length=1000, null=False)
    created_at = models.DateTimeField(null=True)
    pic = models.ImageField(upload_to='house_image', blank=False, null=True)
    estate = models.CharField(max_length=1000, null=False)
    starred = models.BooleanField(default=False)
    # bookmarked = models.BooleanField(default=False)
    bookmarks = models.ManyToManyField(Profile, related_name='bookmarks')


class HouseImage(models.Model):
    pic = models.ImageField(upload_to='house_image', null=True, default=None)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(null=False)
    created_at = models.DateTimeField(null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)



