from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('review', views.review),
    path('deletreview/<int:idobj>', views.deletreview),

    path('addreview', views.addreview),
    path('lensess', views.lensess),
    path('news', views.news),
    path('portfolio', views.portfolio),
    path('frame', views.frame),
    path('organizations', views.organizations)

]