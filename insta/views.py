from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'insta/index.html', {"images":images})

def image_details(request, pk):
    image = Image.objects.get(id=pk)
    return render(request, 'insta/imagedetail.html', {"image":image})
