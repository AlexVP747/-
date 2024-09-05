from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User

class Register(CreateView):
  template_name="login/index.html"
  form_class=UserCreationForm
  model=User
  success_url="/"

class Login(LoginView):
  template_name="login/login.html"
  success_url="login/profile" 

class Profile(TemplateView):
  template_name='Login/profile.html'


