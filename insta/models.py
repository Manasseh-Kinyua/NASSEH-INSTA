import profile
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profilePhoto = models.ImageField(upload_to = 'photos/')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    images = models.ForeignKey("Image", on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.bio

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey("Image", on_delete=models.CASCADE, null=True)
    comment = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    imageName = models.CharField(max_length = 30)
    imageCaption = models.TextField()
    # comments = models.ForeignKey(Comments, on_delete = models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    created = models.DateTimeField(auto_now_add = True, null = True)
    

    def __str__(self):
        return self.imageName