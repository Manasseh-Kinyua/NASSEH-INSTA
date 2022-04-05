from django.db import models

# Create your models here.
class Profile(models.Model):
    profilePhoto = models.ImageField(upload_to = 'profilephotos/')
    bio = models.TextField()