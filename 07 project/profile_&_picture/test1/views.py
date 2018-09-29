from django.shortcuts import render
from .models import Post



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'test1/home.html',context)

def about(request):
    return render(request,'test1/about.html',{'title':'About'})