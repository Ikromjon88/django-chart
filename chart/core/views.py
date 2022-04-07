from django.shortcuts import render
from .models import Post

def home(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, "index.html",context)

def example(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, "examp.html",context)

def linechart(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, "line_chart.html",context)

def piechart(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, "piechart.html",context)

def bubble(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, "buuble.html",context)

def area(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, "area.html",context)