from django.shortcuts import render, redirect
from .models import *
from .form import SignUp
# Create your views here.

def sign_in(request):
    context = {}
    return render(request, 'enroll/sign_in.html', context=context)

def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name', None)
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)
            password1 = form.cleaned_data.get('password2', None)
            print(username, email, password, password1, '******')
            return redirect('signin')
        else:
            pass
        context = {'form': form}
    else:
        form = SignUp()
        context = {'form': form}
    return render(request, 'enroll/sign_up.html', context=context)