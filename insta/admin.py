from django.contrib import admin
from .models import Comments, Image, Profile

# Register your models here.

admin.site.register(Comments)
admin.site.register(Image)
admin.site.register(Profile)