from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Register.as_view()),
    path('login', views.Login.as_view()),
    path('profile', views.Profile.as_view()),
    path('logout', LogoutView.as_view())

    
]