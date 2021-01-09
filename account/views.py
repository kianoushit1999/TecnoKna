from django.http import HttpResponseRedirect
from .models import *
from .form import SignUpForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
# Create your views here.

class sign_in(LoginView):
    redirect_authenticated_user = True
    template_name = 'enroll/sign_in.html'
    success_url = ''

class sign_up(FormView):
    form_class = SignUpForm
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
        user = User(username=user_name, email=email)
        user.set_password(password)
        user.save()
        Phone.objects.create(phone=phone, owner=user)
        return HttpResponseRedirect(self.get_success_url())

class LogOut(LogoutView):
    template_name = None