from django.shortcuts import render, redirect
from .models import Blogger
from .forms import BloggerForm  # Припустимо, ви створили форму BloggerForm

def add_blogger(request):
    if request.method == 'POST':
        form = BloggerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BloggerForm()

    return render(request, 'bloggers/add_blogger.html', {'form': form})

def home(request):
    bloggers = Blogger.objects.all()
    return render(request, 'bloggers/home.html', {'bloggers': bloggers})

def blogger_profiles(request):
    bloggers = Blogger.objects.all()
    return render(request, 'bloggers/blogger_profiles.html', {'bloggers': bloggers})

def blogger_details(request, blogger_id):
    blogger = Blogger.objects.get(id=blogger_id)
    return render(request, 'bloggers/blogger_details.html', {'blogger': blogger})

def news(request):
    # Логіка для отримання останніх новин
    return render(request, 'bloggers/news.html')
