from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def sign_in(request):
    context = {}
    return render(request, 'enroll/sign_in.html', context=context)
def sign_up(request):
    context = {}
    return render(request, 'enroll/sign_up.html', context=context)