from django.shortcuts import render, redirect
from .models import Image
from .forms import CommentForm

# Create your views here.
def index(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'insta/index.html', context)

def image_details(request, pk):
    image = Image.objects.get(id=pk)
    return render(request, 'insta/imagedetail.html', {"image":image})

def comment(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'insta/comment_form.html', context)
