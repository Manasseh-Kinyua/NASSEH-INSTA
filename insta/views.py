from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'insta/index.html', {"images":images})
