from django.shortcuts import render

posts = [
    {'author':'Rahul Shukla',
     'title':'Blog Post 1',
     'content':'First post content',
     'date_posted':'September,2,2018',

    } ,

    {'author':' Shukla',
     'title':'Blog Post 2',
     'content':'Second post content',
     'date_posted':'September,4,2018', }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request,'test1/home.html',context)

def about(request):
    return render(request,'test1/about.html',{'title':'About'})