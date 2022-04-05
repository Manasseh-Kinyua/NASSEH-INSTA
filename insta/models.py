import profile
from django.db import models

# Create your models here.
class Profile(models.Model):
    profilePhoto = models.ImageField(upload_to = 'photos/')
    bio = models.TextField()

    def __str__(self):
        return self.bio

class Comments(models.Model):
        comment = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    imageName = models.CharField(max_length = 30)
    imageCaption = models.TextField()
    comments = models.ForeignKey(Comments, on_delete = models.CASCADE, null = True, blank = True)
    

    def __str__(self):
        return self.imageName