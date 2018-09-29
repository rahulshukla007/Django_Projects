from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'your account has been created, Now you can log-In')
            return redirect ('login')


    else:
        form = RegisterForm()
    return render(request,'test2/register.html',{'form':form})
@login_required
def profile(request):
    return render(request,'test2/profile.html')