from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('review', views.review),
    path('deletreview/<int:idobj>', views.deletreview),
    path('addreview', views.addreview),
    path('lensess', views.lensess),
    path('sale', views.sale),
    path('portfolio', views.portfolio),
    path('frame', views.frame),
    path('organizations', views.organizations),
    path('pdf/<int:id>', views.pdforder)


]