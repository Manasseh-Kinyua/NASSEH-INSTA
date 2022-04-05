from django.shortcuts import render, redirect
from .models import Image
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password does not exist')
        
    context = {
        "page": page
    }
    return render(request, 'insta/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerPage(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'A error Occured during registration')
    return render(request, 'insta/login_register.html', {"form":form})

def index(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'insta/index.html', context)

@login_required(login_url = '/login')
def image_details(request, pk):
    image = Image.objects.get(id=pk)
    return render(request, 'insta/imagedetail.html', {"image":image})

@login_required(login_url = '/login')
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
