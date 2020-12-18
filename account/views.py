from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .form import SignUp
from django.views.generic import FormView
# Create your views here.

def sign_in(request):
    context = {}
    return render(request, 'enroll/sign_in.html', context=context)


class sign_up(FormView):
    form_class = SignUp
    http_method_names = ['get', 'post']
    template_name = 'enroll/sign_up.html'
    success_url = '/signin/'

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        data = self.get_form_kwargs().get('data')
        user_name = data.get('user_name')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')
        user = User(username=user_name, password=password, email=email)
        user.save()
        Phone.objects.create(phone=phone, owner=user)
        return HttpResponseRedirect(self.get_success_url())