from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, f'your account has been created')
            return redirect ('test-home')

    else:
        form = UserCreationForm()
    return render(request,'test2/register.html',{'form':form})
