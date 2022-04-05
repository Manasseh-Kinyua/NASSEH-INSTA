import profile
from django.db import models

# Create your models here.
class Profile(models.Model):
    profilePhoto = models.ImageField(upload_to = 'photos/')
    bio = models.TextField()

    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    imageName = models.CharField(max_length = 30)
    imageCaption = models.TextField()
    # profile = models.ForeignKey(Profile)
    comments = models.TextField()

    def __str__(self):
        return self.imageName