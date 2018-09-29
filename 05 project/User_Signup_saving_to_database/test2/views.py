from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'your account has been created')
            return redirect ('test-home')

    else:
        form = RegisterForm()
    return render(request,'test2/register.html',{'form':form})
