from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User

class Register(CreateView):
  template_name="login/index.html"
  form_class=UserCreationForm
  model=User


